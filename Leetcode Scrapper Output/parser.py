import os 
import json 

def parse_company_data(path): 


    headers = ["problem id", "problem name", "acceptance", "difficulty", "frequency", "url"]
    for i in os.listdir(path): 
        if ".json" in i: 
            
            return_text = ""
            with open(os.path.join(path,i)) as f: 
                data = json.load(f)
                row_list = data["data"]
                final_data = {}
                company_name = i.split(".json")[0]
                
                return_text += f"<h2> {company_name} <h2>"
                return_text += "\n"

                for i in row_list: 
                    duration = i["duration"]
                    
                    if duration not in final_data: 
                        final_data[duration] = []
                    
                    final_data[duration].append(
                    [
                    i["problemData"][0]["problemId"]
                    , i["problemData"][0]["problemName"]
                    , i["problemData"][0]["acceptance"]
                    , i["problemData"][0]["difficulty"]
                    , i["problemData"][0]["frequency"]
                    , i["problemData"][0]["url"]
                    ]
                    )

                for key in final_data: 
                    return_text += f"<h3>{key}<h3>"
                    return_text += "\n"
                    return_text += "\n"
                    return_text += create_markdown_table(headers, final_data[key])
                
                target_path = os.getcwd() + "/parsed company problems"
                file_name = f"{company_name}.md"
                with open(os.path.join(target_path, file_name), "w") as f: 
                    f.write(return_text)
                

def create_markdown_table(headers, rows): 
    text = ""
    for i in headers: 
        text += i
        text += "|"
        
    text += "\n"
    for i in headers: 
        dashes = len(i)*"-"
        text += dashes 
        text += "|"
    text += "\n"

    for row in rows:
        row_text = "" 
        for col in row: 
            row_text += str(col)
            row_text += "|"
        row_text += "\n"
        text += row_text
    return text



def parse_problemsets_data(path): 
    return 


def parse_problems_data(path):
    return 

