from fastapi import FastAPI, Response
import datetime


app = FastAPI(
    title="测试接口",
    description="测试接口",
    version="1.0.0",
)


@app.get("/get_words")
def get_words(response: Response):
    header_list = []
    f1 = open('header.txt', 'r', encoding='utf-8')
    for line in f1:
        line = line.strip()
        header_list.append(line)
    f1.close()
    print(header_list)
    if len(header_list) != 2:
        return "error when reading the header data"
    response.headers["Last-Modified"] = str(header_list[0])
    response.headers["ETag"] = str(header_list[1])
    f = open('data.txt', 'r', encoding='utf-8')
    data = ""
    for line in f:
        data = data + line
    f.close()
    return data


@app.get("/update")
def update_status(tag: str):
    f = open('header.txt', 'w', encoding='utf-8')
    f.write(str(datetime.datetime.now())+'\n')
    f.write(tag)
    f.close()
    return "success"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9375)
