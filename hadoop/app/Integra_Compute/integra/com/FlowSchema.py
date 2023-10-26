from typing import Optional
import pydantic
from pydantic import validator, constr
from enum import Enum
from datetime import date , datetime , timezone
from pyspark.sql.types import StructType, StructField, StringType ,ArrayType , BooleanType , LongType

import uuid

class ConnecStrC(pydantic.BaseModel):
    endPoint : str 
    port : int| None=22
    valutFlag : bool | None = False 
    userID : str
    passwd : str 
    connName: str

class DataSchemaC(pydantic.BaseModel):
    colname : str
    dataType: str
    nullable: bool | None = False
    maxLen : int | None = None
    minLen : int | None = None

class InputMetC(pydantic.BaseModel):
    nodeType : str 
    nodeName : str 
    nodeID : str 
    fileFormat : str
    filename: str 
    folder: str
    connectString: ConnecStrC
    inSchema : list[DataSchemaC] | None=[] 
    outSchema: list[DataSchemaC]  
    backRefs : list[str] | None=[] 
    nextRefs : list[str]  
    cacheFlag: bool | None=False 
    
class WFTYPE_ENUM(str, Enum ):
    WF = 'WF'
    WF_CONN = 'WF_CONN'

class FlowMetaC(pydantic.BaseModel) :
    wfName:str
    wfType: WFTYPE_ENUM| None = WFTYPE_ENUM.WF
    wfId: uuid.UUID 
    ver:str 
    create_date: date|int 
    modified_date:date|int 
    trigger: str | None="default"
    inputNode: list[InputMetC] = []
    
    # @validator('wfId') 
    # def valid_uuid(cls, value ):
    #     try:
    #         uuid.UUID(str(value)) 
    #         return value 
    #     except ValueError:
    #         raise ValueError("NOT VALID UUID") 
        

flowMetaSchema = StructType([ \
    StructField('create_date', StringType(), True),
    StructField('inputNode', ArrayType( StructType([\
            StructField('backRefs', StringType(), True),
            StructField('cacheFlag', BooleanType(), True),\
            StructField('connectString', StructType([\
              StructField('connName', StringType(), True),\
              StructField('endPoint', StringType(), True),\
              StructField('passwd', StringType(), True),\
              StructField('port', StringType(), True), \
              StructField('userID', StringType(), True),\
              StructField('valutFlag', BooleanType(), True)]), True),\
           StructField('fileFormat', StringType(), True),\
           StructField('filename', StringType(), True),\
           StructField('folder', StringType(), True), \
           StructField('inSchema', StringType(), True),\
           StructField('nextRefs', ArrayType(StringType(), True), True),\
           StructField('nodeID', StringType(), True),\
           StructField('nodeName', StringType(), True),\
           StructField('nodeType', StringType(), True),\
           StructField('outSchema', ArrayType(StructType([StructField('colname', StringType(), True), StructField('dataType', StringType(), True), StructField('maxLen', LongType(), True), StructField('minLen', LongType(), True), StructField('nullable', BooleanType(), True)]), True), True)]), True), True),\
           StructField('modified_date', StringType(), True),\
           StructField('trigger', StringType(), True),\
           StructField('ver', StringType(), True),\
           StructField('wfId', StringType(), True), \
           StructField('wfName', StringType(), True), \
           StructField('wfType', StringType(), True)])
