from dataclasses import dataclass
from typing import List

@dataclass
class flowMetadata : 
    wfName : str 
    wfType : str 
    wfId :  str 
    ver : str 
    create_date :str  
    modified_date: int
    create_date : int
    inputNode : List(str)
    functionNode : List(str)
    outputNode : List(str) 

    