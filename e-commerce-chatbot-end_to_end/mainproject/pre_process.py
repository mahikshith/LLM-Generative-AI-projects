
import pandas as pd

from langchain_core.documents import Document

def convert_to_doc():

    df = pd.read_csv(r"../sample_date/flipkart_product_review.csv")

    f_df = df[["product_title","review","summary"]]

    pdt_list =[] 

    for index , row in f_df.iterrows():
        pdt_dict = {}
        pdt_dict["product_title"] = row["product_title"]
        pdt_dict["review"] = row["review"]
        pdt_dict["summary"] = row["summary"]
        pdt_list.append(pdt_dict)
    
    final_doc_data = []
    for each in pdt_list:
        metadata = {"product_title": each["product_title"]}
        final_doc_data.append(Document(page_content= each["review"]+ " "+ each["summary"], metadata=metadata))

    return final_doc_data
