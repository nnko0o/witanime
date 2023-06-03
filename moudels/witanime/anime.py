import json
from typing import List, Dict, Tuple, Optional

from fuzzywuzzy import fuzz, process

class AnimeDBManger:
    def __init__(
          self, 
          db_path:str = None,
        )-> None :
        assert isinstance(db_path, str), '"db_path" must be str, for your db path'
        self.db = self.load_anime_data(db_path)

    def load_anime_data(
          self,
          path:str,
        )-> Dict[str, Dict[str, str]]:
        # Load anime data from a JSON file
        with open(
             path, 
             'r', encoding="utf-8", errors="ignore"
            ) as f:
            return json.load(f)

    def search_anime(
          self,
          anime_name:str,
        )-> List[Tuple[str, int]]:
        # Search for anime name using fuzzywuzzy
        results = process.extract(
            anime_name, 
            self.db.keys(), 
            limit=50, 
            scorer=fuzz.token_set_ratio
        )
        # Filter the results based on the score_cutoff of 85
        filtered_results = filter(lambda x: x[1] >= 85, results)
        results = list(filtered_results)

        returned = [] # {name:str, eps:List[str]}
        for key in results :
            returned.append({
                "name":key[0],
                "filter_score":key[1],
                "eps":self.db.get(key[0]).values(),
            },)
        
        return returned

    def get_anime(self, key:str)-> Optional[List[str]]:
        print(key)
        anime_eps = self.db.get(key)
        if anime_eps is None:
            return None

        return {
           "name":key,
           "eps":anime_eps.values()
        }
