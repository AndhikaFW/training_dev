from typing import Annotated
from fastapi import FastAPI, File, UploadFile, Form, Request, WebSocket
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv                                 
import os
load_dotenv()                                                  
api_key = os.getenv("OPENAI_API_KEY")
checkpause = os.getenv("PAUSE")
from openai import OpenAI
from llama_index.core import SQLDatabase
from llama_index.llms.openai import OpenAI
scoreshow=[""]
scorescript=[""]
scores=[]
courseshow=[""]
coursescript=[""]
courses=[]
coursereq=[]
userscores=[]
userscoresthead=[]
userscoreshow=[]
chatarea=[]
usercourses=[]
n0=0
n1=0
train_dev = FastAPI()

train_dev.mount("/static", StaticFiles(directory="static"), name="static")

def upCourse(id, name, desc):
    global courses, courseshow, coursescript;
    courses.insert(id*3, id)
    courses.insert(id*3+1, name)
    courses.insert(id*3+2, desc)
    fill = f"""
        <div class="pure-u-1-2">
            <div class="course">
                <form action="/deletecourse" id="remove{id}" enctype="application/x-www-form-urlencoded" method="post"><input type="hidden" id="id" name="id" value="{id}" /></form>
                <form action="/addcourse" id="remove{id}" enctype="application/x-www-form-urlencoded" method="post">
                <div class="pure-g dropbtn">
                    <div class="pure-u-3-5">
                        <input type="text" name="name" id="name" class="scorename" placeholder="" value="{name}">
                    </div>
                    <div class="pure-u-1-5">
                        <button class="transparent-button"> 
                            <svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" viewBox="0 0 24 24"><path fill="none" stroke="white" stroke-dasharray="24" stroke-dashoffset="24" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 11L11 17L21 7"><animate fill="freeze" attributeName="stroke-dashoffset" dur="0.4s" values="24;0"/></path></svg>
                        </button> 
                    </div>
                    <div class="pure-u-1-5">
                        <svg onclick="remove{id}()" xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" viewBox="0 0 24 24"><g fill="none" stroke="white" stroke-dasharray="22" stroke-dashoffset="22" stroke-linecap="round" stroke-width="2"><path d="M19 5L5 19"><animate fill="freeze" attributeName="stroke-dashoffset" begin="0.3s" dur="0.3s" values="22;0"/></path><path d="M5 5L19 19"><animate fill="freeze" attributeName="stroke-dashoffset" dur="0.3s" values="22;0"/></path></g></svg>
                    </div>
                </div>
                <div class="desc">
                    <textarea name="desc" id="desc">{desc}</textarea>
                </div>
                <input type="hidden" id="id" name="id" value="{id}" />
                </form>
            </div>
        </div>
    """
    courseshow.insert(id,fill)
    functions= f"""
        function remove{id}(){{
            document.getElementById("remove{id}").submit();
        }}
    """
    coursescript.insert(id,functions)

def upScore(id, name, score0, score1, score2, score3, score4, score5, score6, score7, score8, score9, score10):
    global scores, scoreshow, scorescript, userscores, userscoresthead
    scores.insert(id*13, id)
    scores.insert(id*13+1, name)
    scores.insert(id*13+2, score0)
    scores.insert(id*13+3, score1)
    scores.insert(id*13+4, score2)
    scores.insert(id*13+5, score3)
    scores.insert(id*13+6, score4)
    scores.insert(id*13+7, score5)
    scores.insert(id*13+8, score6)
    scores.insert(id*13+9, score7)
    scores.insert(id*13+10, score8)
    scores.insert(id*13+11, score9)
    scores.insert(id*13+12, score10)
    userscores.insert(id, 10)
    content = f"""<form action="/removeindicator" id="remove{id}" enctype="application/x-www-form-urlencoded" method="post" class="hide"><input type="hidden" id="id" name="id" value="{id}" /></form><form action="/postcriteria" enctype="application/x-www-form-urlencoded" method="post"><div class="pure-g dropbtn"><div class="pure-u-20-24"><input type="text" name="name" id="name" class="scorename" placeholder="" value="{name}"></div><div class="pure-u-2-24"><svg onclick="form{id}()" id="{id}rot180" class="rotate" style="width:100%;" xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" viewBox="0 0 24 24"><g transform="rotate(-90 12 12)"><g fill="none" stroke="white" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"><path stroke-dasharray="20" stroke-dashoffset="20" d="M21 12H3.5"><animate fill="freeze" attributeName="stroke-dashoffset" dur="0.3s" values="20;0"/></path><path stroke-dasharray="12" stroke-dashoffset="12" d="M3 12L10 19M3 12L10 5"><animate fill="freeze" attributeName="stroke-dashoffset" begin="0.3s" dur="0.2s" values="12;0"/></path></g></g></svg></div><div class="pure-u-2-24"><svg onclick="remove{id}()" xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" viewBox="0 0 24 24"><g fill="none" stroke="white" stroke-dasharray="22" stroke-dashoffset="22" stroke-linecap="round" stroke-width="2"><path d="M19 5L5 19"><animate fill="freeze" attributeName="stroke-dashoffset" begin="0.3s" dur="0.3s" values="22;0"/></path><path d="M5 5L19 19"><animate fill="freeze" attributeName="stroke-dashoffset" dur="0.3s" values="22;0"/></path></g></svg></div></div><div id="form{id}" class="dropdown-content"><div class="pure-g"><div class="pure-u-1-12"></div><div class="pure-u-11-12">Isi data penilaian anda:</div></div><div class="pure-g"><div class="pure-u-2-24"><p><b>0 :</b></p></div><div class="pure-u-21-24"><input type="text" name="score0" id="score0" value="{score0}"></div><div class="pure-u-1-24"></div></div><div class="pure-g"><div class="pure-u-2-24"><p><b>0.1 :</b></p></div><div class="pure-u-21-24"><input type="text" name="score1" id="score1" value="{score1}"></div><div class="pure-u-1-24"></div></div><div class="pure-g"><div class="pure-u-2-24"><p><b>0.2 :</b></p></div><div class="pure-u-21-24"><input type="text" name="score2" id="score2" value="{score2}"></div><div class="pure-u-1-24"></div></div><div class="pure-g"><div class="pure-u-2-24"><p><b>0.3 :</b></p></div><div class="pure-u-21-24"><input type="text" name="score3" id="score3" value="{score3}"></div><div class="pure-u-1-24"></div></div><div class="pure-g"><div class="pure-u-2-24"><p><b>0.4 :</b></p></div><div class="pure-u-21-24"><input type="text" name="score4" id="score4" value="{score4}"></div><div class="pure-u-1-24"></div></div><div class="pure-g"><div class="pure-u-2-24"><p><b>0.5 :</b></p></div><div class="pure-u-21-24"><input type="text" name="score5" id="score5" value="{score5}"></div><div class="pure-u-1-24"></div></div><div class="pure-g"><div class="pure-u-2-24"><p><b>0.6 :</b></p></div><div class="pure-u-21-24"><input type="text" name="score6" id="score6" value="{score6}"></div><div class="pure-u-1-24"></div></div><div class="pure-g"><div class="pure-u-2-24"><p><b>0.7 :</b></p></div><div class="pure-u-21-24"><input type="text" name="score7" id="score7" value="{score7}"></div><div class="pure-u-1-24"></div></div><div class="pure-g"><div class="pure-u-2-24"><p><b>0.8 :</b></p></div><div class="pure-u-21-24"><input type="text" name="score8" id="score8" value="{score8}"></div><div class="pure-u-1-24"></div></div><div class="pure-g"><div class="pure-u-2-24"><p><b>0.9 :</b></p></div><div class="pure-u-21-24"><input type="text" name="score9" id="score9" value="{score9}"></div><div class="pure-u-1-24"></div></div><div class="pure-g"><div class="pure-u-2-24"><p><b>1 :</b></p></div><div class="pure-u-21-24"><input type="text" name="score10" id="score10" value="{score10}"></div><div class="pure-u-1-24"></div></div><div class="pure-g"><div class="pure-u-1-12"></div><div class="pure-u-4-5"><button id="post" class="pure-button blue-button">Submit</button></div></div></div><input type="hidden" id="id" name="id" value="{id}" /></form></br>"""
    scoreshow.insert(id,content)
    functions= f"""
        function form{id}() {{
            document.getElementById("form{id}").classList.toggle("show");
            document.getElementById("{id}rot180").classList.toggle("rotate180");
            document.getElementById("form{id}").scrollIntoView({{ block: "center", behavior: 'smooth' }});
        }}

        function remove{id}(){{
            document.getElementById("remove{id}").submit();
        }}
    """
    scorescript.insert(id,functions)
    thead = f"""<th>{name}</th>"""
    userscoresthead.insert(id, thead)



default=["""<!DOCTYPE html><html lang="en"><head><title>Training&Development</title><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><link href="static/css/styles.css" rel="stylesheet"><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/purecss@3.0.0/build/pure-min.css" integrity="sha384-X38yfunGUhNzHpBaEBsWLO+A0HDYOQi8ufWDkZ0k9e0eXz/tH3II7uKZ9msv++Ls" crossorigin="anonymous"><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/purecss@3.0.0/build/grids-responsive-min.css"></head><body><div id="layout"><!-- Menu toggle --><a href="#menu" id="menuLink" class="menu-link"><!-- Hamburger icon --><span></span></a><div id="menu"><div class="pure-menu"><a class="pure-menu-heading" href="https://github.com/AndhikaFW" target="_blank" rel="noopener noreferrer">@NORU</a><ul class="pure-menu-list"><li class="pure-menu-item dropbtn"><a href="/"><div id="menu0" class="pure-g""",
         """"><div class="pure-u-1-5"><svg xmlns="http://www.w3.org/2000/svg" width="4em" height="4em" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><g stroke-width="2"><path stroke-dasharray="66" stroke-dashoffset="66" d="M12 3H19V21H5V3H12Z"><animate fill="freeze" attributeName="stroke-dashoffset" dur="0.6s" values="66;0"/></path><path stroke-dasharray="5" stroke-dashoffset="5" d="M9 10H12"><animate fill="freeze" attributeName="stroke-dashoffset" begin="1s" dur="0.2s" values="5;0"/></path><path stroke-dasharray="6" stroke-dashoffset="6" d="M9 13H14"><animate fill="freeze" attributeName="stroke-dashoffset" begin="1.2s" dur="0.2s" values="6;0"/></path><path stroke-dasharray="7" stroke-dashoffset="7" d="M9 16H15"><animate fill="freeze" attributeName="stroke-dashoffset" begin="1.4s" dur="0.2s" values="7;0"/></path></g><path stroke-dasharray="12" stroke-dashoffset="12" d="M14.5 3.5V6.5H9.5V3.5"><animate fill="freeze" attributeName="stroke-dashoffset" begin="0.7s" dur="0.2s" values="12;0"/></path></g></svg></div><div class="pure-u-4-5"><h3>| Isi Kriteria</h3></div></div></a></li><li class="pure-menu-item dropbtn"><a href="/scores"><div id="menu1" class="pure-g""",
         """"><div class="pure-u-1-5"><svg xmlns="http://www.w3.org/2000/svg" width="4em" height="4em" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-dasharray="32" stroke-dashoffset="32" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3L9.65 8.76L3.44 9.22L8.2 13.24L6.71 19.28L12 16M12 3L14.35 8.76L20.56 9.22L15.8 13.24L17.29 19.28L12 16"><animate fill="freeze" attributeName="stroke-dashoffset" dur="0.5s" values="32;0"/></path><path fill="currentColor" fill-opacity="0" d="M12 3L9.65 8.76L3.44 9.22L8.2 13.24L6.71 19.28L12 16Z"><animate fill="freeze" attributeName="fill-opacity" begin="0.5s" dur="0.5s" values="0;1"/></path></svg></div><div class="pure-u-4-5"><h3>| Skor Pegawai</h3></div></div></a></li><li class="pure-menu-item dropbtn"><a href="/courses"><div id="menu2" class="pure-g""",
         """"><div class="pure-u-1-5"><svg xmlns="http://www.w3.org/2000/svg" width="4em" height="4em" viewBox="0 0 24 24"><g fill="currentColor"><path fill-opacity="0" stroke="currentColor" stroke-dasharray="46" stroke-dashoffset="46" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 17H9V14.1973C7.2066 13.1599 6 11.2208 6 9C6 5.68629 8.68629 3 12 3C15.3137 3 18 5.68629 18 9C18 11.2208 16.7934 13.1599 15 14.1973V17z"><animate fill="freeze" attributeName="stroke-dashoffset" dur="0.4s" values="46;0"/><animate fill="freeze" attributeName="fill-opacity" begin="0.7s" dur="0.5s" values="0;1"/></path><rect width="6" height="0" x="9" y="20" rx="1"><animate fill="freeze" attributeName="height" begin="0.5s" dur="0.2s" values="0;2"/></rect></g></svg></div><div class="pure-u-4-5"><h3>| Training</h3></div></div></a></li><li class="pure-menu-item dropbtn"><a href="/process"><div id="menu3" class="pure-g""",
         """"><div class="pure-u-1-5"><svg xmlns="http://www.w3.org/2000/svg" width="4em" height="4em" viewBox="0 0 24 24"><path fill="currentColor" fill-opacity="0" stroke="currentColor" stroke-dasharray="36" stroke-dashoffset="36" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 6L18 12L8 18z"><animate fill="freeze" attributeName="stroke-dashoffset" dur="0.4s" values="36;0"/><animate fill="freeze" attributeName="fill-opacity" begin="0.5s" dur="0.5s" values="0;1"/></path></svg></div><div class="pure-u-4-5"><h3>| Proses</h3></div></div></a></li><li class="pure-menu-item dropbtn"><a href="/settings"><div id="menu4" class="pure-g""",
         """"><div class="pure-u-1-5"><svg xmlns="http://www.w3.org/2000/svg" width="4em" height="4em" viewBox="0 0 24 24"><defs><symbol id="lineMdCogFilledLoop0"><path fill="#fff" d="M11 13L15.74 5.5C16.03 5.67 16.31 5.85 16.57 6.05C16.57 6.05 16.57 6.05 16.57 6.05C16.64 6.1 16.71 6.16 16.77 6.22C18.14 7.34 19.09 8.94 19.4 10.75C19.41 10.84 19.42 10.92 19.43 11C19.43 11 19.43 11 19.43 11C19.48 11.33 19.5 11.66 19.5 12z"><animate fill="freeze" attributeName="d" begin="0.5s" dur="0.2s" values="M11 13L15.74 5.5C16.03 5.67 16.31 5.85 16.57 6.05C16.57 6.05 16.57 6.05 16.57 6.05C16.64 6.1 16.71 6.16 16.77 6.22C18.14 7.34 19.09 8.94 19.4 10.75C19.41 10.84 19.42 10.92 19.43 11C19.43 11 19.43 11 19.43 11C19.48 11.33 19.5 11.66 19.5 12z;M11 13L15.74 5.5C16.03 5.67 16.31 5.85 16.57 6.05C16.57 6.05 19.09 5.04 19.09 5.04C19.25 4.98 19.52 5.01 19.6 5.17C19.6 5.17 21.67 8.75 21.67 8.75C21.77 8.92 21.73 9.2 21.6 9.32C21.6 9.32 19.43 11 19.43 11C19.48 11.33 19.5 11.66 19.5 12z"/></path></symbol><mask id="lineMdCogFilledLoop1"><path fill="none" stroke="#fff" stroke-dasharray="36" stroke-dashoffset="36" stroke-width="5" d="M12 7C14.76 7 17 9.24 17 12C17 14.76 14.76 17 12 17C9.24 17 7 14.76 7 12C7 9.24 9.24 7 12 7z"><animate fill="freeze" attributeName="stroke-dashoffset" dur="0.4s" values="36;0"/><set attributeName="opacity" begin="0.4s" to="0"/></path><g opacity="0"><use href="#lineMdCogFilledLoop0"/><use href="#lineMdCogFilledLoop0" transform="rotate(60 12 12)"/><use href="#lineMdCogFilledLoop0" transform="rotate(120 12 12)"/><use href="#lineMdCogFilledLoop0" transform="rotate(180 12 12)"/><use href="#lineMdCogFilledLoop0" transform="rotate(240 12 12)"/><use href="#lineMdCogFilledLoop0" transform="rotate(300 12 12)"/><set attributeName="opacity" begin="0.4s" to="1"/><animateTransform attributeName="transform" dur="30s" repeatCount="indefinite" type="rotate" values="0 12 12;360 12 12"/></g><circle cx="12" cy="12" r="3.5"/></mask></defs><rect width="24" height="24" fill="currentColor" mask="url(#lineMdCogFilledLoop1)"/></svg></div><div class="pure-u-4-5"><h3>| Pengaturan</h3></div></div></a></li></ul></div></div><div class="content">""",
         """<script src="static/js/ui.js"></script></body></html>"""
        ]

def courseAnalysis(id, id0):
    global scores, courses, coursereq

    from sqlalchemy import (
        create_engine,
        MetaData,
        Table,
        Column,
        String,
        Integer,
        select,
    )
    engine = create_engine("sqlite:///:memory:")
    metadata_obj = MetaData()
    # create point SQL table
    table_name = "point_stats"
    point_stats_table = Table(
        table_name,
        metadata_obj,
        Column("point_name", Integer, primary_key=True)
    )
    metadata_obj.create_all(engine)

    llm = OpenAI(temperature=0.1, model="gpt-3.5-turbo")

    sql_database = SQLDatabase(engine, include_tables=["point_stats"])

    from sqlalchemy import insert
    
    rows = [
        {"point_name": 0},
        {"point_name": 1},
        {"point_name": 2},
        {"point_name": 3},
        {"point_name": 4},
        {"point_name": 5},
        {"point_name": 6},
        {"point_name": 7},
        {"point_name": 8},
        {"point_name": 9},
        {"point_name": 10},
    ]
    for row in rows:
        stmt = insert(point_stats_table).values(**row)
        with engine.begin() as connection:
            cursor = connection.execute(stmt)
    # view current table
    stmt = select(
        point_stats_table.c.point_name
    ).select_from(point_stats_table)

    with engine.connect() as connection:
        results = connection.execute(stmt).fetchall()
    
    from sqlalchemy import text

    with engine.connect() as con:
        rows = con.execute(text("SELECT point_name from point_stats"))

    from llama_index.core.query_engine import NLSQLTableQueryEngine

    query_engine = NLSQLTableQueryEngine(
        sql_database=sql_database, tables=["point_stats"], llm=llm
    )
    query_str = f"{scores[id*13+2]} bernilai 0. {scores[id*13+3]} bernilai 1. {scores[id*13+4]} bernilai 2. {scores[id*13+5]} bernilai 3. {scores[id*13+6]} bernilai 4. {scores[id*13+7]} bernilai 5. {scores[id*13+8]} bernilai 6. {scores[id*13+9]} bernilai 7. {scores[id*13+10]} bernilai 8. {scores[id*13+11]} bernilai 9. {scores[id*13+12]} bernilai 10. Berapa nilai terkecil yang cocok dengan kursus {courses[id0+1]} dimana {courses[id0+1]} merupakan {courses[id0+2]}"
    response = query_engine.query(query_str)
    result = response.metadata["result"] 
    res = int(''.join(map(str, result[0])))
    coursereq.insert(id, res)

def userAnalysis(id, text):
    global scores, courses, userscores, userscoreshow, usercourses, coursereq

    from sqlalchemy import (
        create_engine,
        MetaData,
        Table,
        Column,
        String,
        Integer,
        select,
    )
    engine = create_engine("sqlite:///:memory:")
    metadata_obj = MetaData()
    # create point SQL table
    table_name = "point_stats"
    point_stats_table = Table(
        table_name,
        metadata_obj,
        Column("point_name", Integer, primary_key=True)
    )
    metadata_obj.create_all(engine)

    llm = OpenAI(temperature=0.1, model="gpt-3.5-turbo")

    sql_database = SQLDatabase(engine, include_tables=["point_stats"])

    from sqlalchemy import insert
    
    rows = [
        {"point_name": 0},
        {"point_name": 1},
        {"point_name": 2},
        {"point_name": 3},
        {"point_name": 4},
        {"point_name": 5},
        {"point_name": 6},
        {"point_name": 7},
        {"point_name": 8},
        {"point_name": 9},
        {"point_name": 10},
    ]
    for row in rows:
        stmt = insert(point_stats_table).values(**row)
        with engine.begin() as connection:
            cursor = connection.execute(stmt)
    # view current table
    stmt = select(
        point_stats_table.c.point_name
    ).select_from(point_stats_table)

    with engine.connect() as connection:
        results = connection.execute(stmt).fetchall()
    
    from sqlalchemy import text

    with engine.connect() as con:
        rows = con.execute(text("SELECT point_name from point_stats"))

    from llama_index.core.query_engine import NLSQLTableQueryEngine

    query_engine = NLSQLTableQueryEngine(
        sql_database=sql_database, tables=["point_stats"], llm=llm
    )
    query_str = f"{scores[id*13+2]} bernilai 0. {scores[id*13+3]} bernilai 1. {scores[id*13+4]} bernilai 2. {scores[id*13+5]} bernilai 3. {scores[id*13+6]} bernilai 4. {scores[id*13+7]} bernilai 5. {scores[id*13+8]} bernilai 6. {scores[id*13+9]} bernilai 7. {scores[id*13+10]} bernilai 8. {scores[id*13+11]} bernilai 9. {scores[id*13+12]} bernilai 10. Berapa nilai yang paling cocok dengan pernyataan {text}"
    response = query_engine.query(query_str)
    result = response.metadata["result"]
    res = int(''.join(map(str, result[0])))
    userscores.insert(id, res)
    content = f"""<td>{res}</td>"""
    userscoreshow.insert(id, content)
    fill = f"""
            <div class="big-course">
                <div class="pure-g dropbtn">
                    <div class="pure-u-1 center">
                        <h1>{courses[id*3+1]}</h1>
                    </div>
                </div>
                <div class="desc">
                    <textarea name="desc" id="desc">{courses[id*3+2]}</textarea>
                </div>
                <input type="hidden" id="id" name="id" value="{courses[id*3]}" />
            </div>
    """
    if int(res)<int(coursereq[id]):
        usercourses.append(fill)


@train_dev.post("/postcriteria")
async def points(id: Annotated[int, Form()], name: Annotated[str, Form()], score0: Annotated[str, Form()], score1: Annotated[str, Form()], score2: Annotated[str, Form()], score3: Annotated[str, Form()], score4: Annotated[str, Form()], score5: Annotated[str, Form()], score6: Annotated[str, Form()], score7: Annotated[str, Form()], score8: Annotated[str, Form()], score9: Annotated[str, Form()], score10: Annotated[str, Form()]):
    global n0, scores, scoreshow, scorescript
    match id:
        case -1:
            id=n0
            n0+=1
        case _:
            scoreshow.pop(id)
            scores.pop(id)
            scorescript.pop(id)

    upScore(id, name, score0, score1, score2, score3, score4, score5, score6, score7, score8, score9, score10)
    return {"id": id, "name": name, "score0": score0, "score1": score1, "score2": score2, "score3": score3, "score4": score4, "score5": score5, "score6": score6, "score7": score7, "score8": score8, "score9": score9, "score10": score10,}
        
@train_dev.post("/removeindicator")
async def points(id: Annotated[int, Form()]):
    global scoreshow, scores
    scoreshow.pop(id)
    scores.pop(id)

@train_dev.post("/addcourse")
async def points(id: Annotated[int, Form()], name: Annotated[str, Form()], desc: Annotated[str, Form()]):
    global n1, courses, courseshow, coursescript;
    match id:
        case -1:
            id=n1
            n1+=1
        case _:
            courseshow.pop(id)
            courses.pop(id)
            coursescript.pop(id)
    upCourse(id, name, desc)
    return {"id": id, "name": name, "desc": desc,}

@train_dev.post("/deletecourse")
async def points(id: Annotated[int, Form()]):
    global courseshow, courses
    courseshow.pop(id)
    courses.pop(id)


@train_dev.get("/")
async def main():
        global scoreshow, scorescript
        pagecontent = f"""{default[0]} selected{default[1]}{default[2]}{default[3]}{default[4]}{default[5]}
            <h1>Kriteria Penilaian</h1>
            <br>
            { ''.join(scoreshow) }
            <br>
            <svg onclick="addVar()" id="rot45" class="dropbtn floatbtn rotate" xmlns="http://www.w3.org/2000/svg" width="3.3em" height="3.3em" viewBox="0 0 24 24"><g fill="none" stroke="white" stroke-dasharray="18" stroke-dashoffset="18" stroke-linecap="round" stroke-width="2"><path d="M12 5V19"><animate fill="freeze" attributeName="stroke-dashoffset" begin="0.4s" dur="0.3s" values="18;0"/></path><path d="M5 12H19"><animate fill="freeze" attributeName="stroke-dashoffset" dur="0.3s" values="18;0"/></path></g></svg>
            <div id="newform" class="dropdown-content">
                <form action="/postcriteria" enctype="application/x-www-form-urlencoded" method="post">
                    <div class="pure-g dropbtn">
                        <div class="pure-u-11-12">
                            <input type="text" name="name" id="name" class="scorename" placeholder="New Indicator">
                        </div>
                        <div class="pure-u-1-12">
                            <svg onclick="addVar()" xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" viewBox="0 0 24 24"><g fill="none" stroke="white" stroke-dasharray="22" stroke-dashoffset="22" stroke-linecap="round" stroke-width="2"><path d="M19 5L5 19"><animate fill="freeze" attributeName="stroke-dashoffset" begin="0.3s" dur="0.3s" values="22;0"/></path><path d="M5 5L19 19"><animate fill="freeze" attributeName="stroke-dashoffset" dur="0.3s" values="22;0"/></path></g></svg>
                        </div>
                    </div>
                    <div class="pure-g"><div class="pure-u-1-12"></div><div class="pure-u-11-12">Isi data penilaian anda:</div></div>
                    <div class="pure-g">
                        <div class="pure-u-2-24"><p><b>0 :</b></p></div>
                        <div class="pure-u-21-24"><input type="text" name="score0" id="score0" placeholder=""></div>
                        <div class="pure-u-1-24"></div>
                    </div>
                    <div class="pure-g">
                        <div class="pure-u-2-24"><p><b>0.1 :</b></p></div>
                        <div class="pure-u-21-24"><input type="text" name="score1" id="score1" placeholder=""></div>
                        <div class="pure-u-1-24"></div>
                    </div>
                    <div class="pure-g">
                        <div class="pure-u-2-24"><p><b>0.2 :</b></p></div>
                        <div class="pure-u-21-24"><input type="text" name="score2" id="score2" placeholder=""></div>
                        <div class="pure-u-1-24"></div>
                    </div>
                    <div class="pure-g">
                        <div class="pure-u-2-24"><p><b>0.3 :</b></p></div>
                        <div class="pure-u-21-24"><input type="text" name="score3" id="score3" placeholder=""></div>
                        <div class="pure-u-1-24"></div>
                    </div>
                    <div class="pure-g">
                        <div class="pure-u-2-24"><p><b>0.4 :</b></p></div>
                        <div class="pure-u-21-24"><input type="text" name="score4" id="score4" placeholder=""></div>
                        <div class="pure-u-1-24"></div>
                    </div>
                    <div class="pure-g">
                        <div class="pure-u-2-24"><p><b>0.5 :</b></p></div>
                        <div class="pure-u-21-24"><input type="text" name="score5" id="score5" placeholder=""></div>
                        <div class="pure-u-1-24"></div>
                    </div>
                    <div class="pure-g">
                    <div class="pure-u-2-24"><p><b>0.6 :</b></p></div>
                        <div class="pure-u-21-24"><input type="text" name="score6" id="score6" placeholder=""></div>
                        <div class="pure-u-1-24"></div>
                    </div>
                    <div class="pure-g">
                        <div class="pure-u-2-24"><p><b>0.7 :</b></p></div>
                        <div class="pure-u-21-24"><input type="text" name="score7" id="score7" placeholder=""></div>
                        <div class="pure-u-1-24"></div>
                    </div>
                    <div class="pure-g">
                        <div class="pure-u-2-24"><p><b>0.8 :</b></p></div>
                        <div class="pure-u-21-24"><input type="text" name="score8" id="score8" placeholder=""></div>
                        <div class="pure-u-1-24"></div>
                    </div>
                    <div class="pure-g">
                        <div class="pure-u-2-24"><p><b>0.9 :</b></p></div>
                        <div class="pure-u-21-24"><input type="text" name="score9" id="score9" placeholder=""></div>
                        <div class="pure-u-1-24"></div>
                    </div>
                    <div class="pure-g">
                        <div class="pure-u-2-24"><p><b>1 :</b></p></div>
                        <div class="pure-u-21-24"><input type="text" name="score10" id="score10" placeholder=""></div>
                        <div class="pure-u-1-24"></div>
                    </div>
                    <div class="pure-g">
                        <div class="pure-u-1-12"></div>
                            <div class="pure-u-4-5"><button id="post" class="pure-button blue-button">Submit</button></div>
                        </div>
                    <input type="hidden" id="id" name="id" value="-1" />
                </form>
            </div>                                              
        </div>
        </div>
        <script>
        function addVar() {{
            document.getElementById("newform").classList.toggle("show");
            document.getElementById("rot45").classList.toggle("rotate45");
            document.getElementById("newform").scrollIntoView({{ block: "center", behavior: 'smooth' }});
        }}{ ''.join(scorescript) }
        </script>{default[6]}"""                                                                                                                                                                                                 
        return HTMLResponse(content=pagecontent)
@train_dev.get("/scores")
async def main():
        global userscoreshow, userscoresthead
        pagecontent = f"""{default[0]}{default[1]} selected{default[2]}{default[3]}{default[4]}{default[5]}
            <table class="pure-table pure-table-horizontal">
                <thead>
                    <tr>
                    {''.join(userscoresthead)}
                    </tr>
                </thead>
                <tbody>
                    <tr>
                    {''.join(userscoreshow)}
                    </tr>
                </tbody>
            </table>
        </div>{default[6]}"""                                                                                                                                                                                                  
        return HTMLResponse(content=pagecontent)

@train_dev.get("/courses")
async def main():
        global courseshow, coursescript
        pagecontent = f"""{default[0]}{default[1]}{default[2]} selected{default[3]}{default[4]}{default[5]}
        <div class="pure-g">
        { ''.join(courseshow) }
        </div>
        <a href="/newcourse"><svg class="dropbtn floatbtn" xmlns="http://www.w3.org/2000/svg" width="3.3em" height="3.3em" viewBox="0 0 24 24"><g fill="none" stroke="white" stroke-dasharray="18" stroke-dashoffset="18" stroke-linecap="round" stroke-width="2"><path d="M12 5V19"><animate fill="freeze" attributeName="stroke-dashoffset" begin="0.4s" dur="0.3s" values="18;0"/></path><path d="M5 12H19"><animate fill="freeze" attributeName="stroke-dashoffset" dur="0.3s" values="18;0"/></path></g></svg></a>
        </div>
        <script>
        { ''.join(coursescript) }
        </script>
        {default[6]}"""                                                                                                                                                                                                 
        return HTMLResponse(content=pagecontent)
@train_dev.get("/newcourse")
async def main():
        pagecontent = f"""{default[0]}{default[1]}{default[2]} selected{default[3]}{default[4]}{default[5]}
        <form action="/addcourse" enctype="multipart/form-data" method="post">
            <div class="pure-g dropbtn">
                <div class="pure-u-22-24">
                    <input type="text" name="name" id="name" class="scorename" placeholder="New Course">
                </div>
                <div class="pure-u-2-24">
                <div onclick="history.back()">
                    <svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" viewBox="0 0 24 24"><g fill="none" stroke="white" stroke-dasharray="22" stroke-dashoffset="22" stroke-linecap="round" stroke-width="2"><path d="M19 5L5 19"><animate fill="freeze" attributeName="stroke-dashoffset" begin="0.3s" dur="0.3s" values="22;0"/></path><path d="M5 5L19 19"><animate fill="freeze" attributeName="stroke-dashoffset" dur="0.3s" values="22;0"/></path></g></svg>
                </div>
                </div>
            </div>
            <div class="box-content">
                <div class="pure-g">
                    <div class="pure-u-1-24"></div>
                    <div class="pure-u-22-24"><textarea name="desc" id="desc" placeholder="Description" class="bigtext"></textarea></div>
                    <div class="pure-u-1-24"></div>
                </div>
                <div class="pure-g">
                    <div class="pure-u-1-12"></div>
                    <div class="pure-u-4-5"><button id="post" class="pure-button blue-button fullbtn">Save</button></div></div>
                    <input type="hidden" id="id" name="id" value="-1" />
                </div>
            </div>
        </form>
        </script>{default[6]}"""                                                                                                                                                                                                  
        return HTMLResponse(content=pagecontent)

@train_dev.get("/process")
async def main():
    id0=0
    id=0
    global n1, coursereq
    for id0 in range(n1):
        for id in range(n0):
            courseAnalysis(id, id0)

    pagecontent = f"""{default[0]}{default[1]}{default[2]}{default[3]} selected{default[4]}{default[5]}
        <form action="/prompt/" enctype="multipart/form-data" method="post">
            <div class="pure-g dropbtn">
                <div class="pure-u-1">
                    <h1>Output</h1>
                </div>
            </div>
            <div id="logs" class="box-content logs">
                <div class="pure-g">
                    <div class="pure-u-1">
                    {coursereq}</div>
                </div>
            </div>
        </form>
    </div>
    {default[6]}"""                                                                                                                                                                                                  
    return HTMLResponse(content=pagecontent)

@train_dev.get("/settings")
async def main():
        pagecontent = f"""{default[0]}{default[1]}{default[2]}{default[3]}{default[4]} selected{default[5]}
            <form action="/prompt/" enctype="multipart/form-data" method="post">
                <div class="pure-g dropbtn" onclick="forecastList()">
                    <div class="pure-u-22-24">
                        Sumber forecast
                    </div>
                    <div class="pure-u-2-24">
                        <svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" viewBox="0 0 24 24"><g fill="currentColor" fill-opacity="0" stroke="currentColor" stroke-linecap="round"><g stroke-dasharray="10" stroke-dashoffset="10"><circle cx="5" cy="5" r="1.5"><animate fill="freeze" attributeName="stroke-dashoffset" dur="0.2s" values="10;0"/><animate fill="freeze" attributeName="fill-opacity" begin="2.0s" dur="0.5s" values="0;1"/></circle><circle cx="5" cy="12" r="1.5"><animate fill="freeze" attributeName="stroke-dashoffset" begin="0.7s" dur="0.2s" values="10;0"/><animate fill="freeze" attributeName="fill-opacity" begin="2.2s" dur="0.5s" values="0;1"/></circle><circle cx="5" cy="19" r="1.5"><animate fill="freeze" attributeName="stroke-dashoffset" begin="1.4s" dur="0.2s" values="10;0"/><animate fill="freeze" attributeName="fill-opacity" begin="2.4s" dur="0.5s" values="0;1"/></circle></g><g stroke-dasharray="28" stroke-dashoffset="28"><rect width="11" height="3" x="9.5" y="3.5" rx="1.5"><animate fill="freeze" attributeName="stroke-dashoffset" begin="0.1s" dur="0.5s" values="28;0"/><animate fill="freeze" attributeName="fill-opacity" begin="2.0s" dur="0.5s" values="0;1"/></rect><rect width="11" height="3" x="9.5" y="10.5" rx="1.5"><animate fill="freeze" attributeName="stroke-dashoffset" begin="0.8s" dur="0.5s" values="28;0"/><animate fill="freeze" attributeName="fill-opacity" begin="2.2s" dur="0.5s" values="0;1"/></rect><rect width="11" height="3" x="9.5" y="17.5" rx="1.5"><animate fill="freeze" attributeName="stroke-dashoffset" begin="1.5s" dur="0.5s" values="28;0"/><animate fill="freeze" attributeName="fill-opacity" begin="2.4s" dur="0.5s" values="0;1"/></rect></g></g></svg>
                    </div>
                </div>
                <div id="forecast" class="dropdown-content">
                    <div class="pure-g">
                        <div class="pure-u-1-24"></div>
                        <div class="pure-u-22-24"><textarea name="title" id="title" placeholder=""></textarea></div>
                        <div class="pure-u-1-24"></div>
                    </div>
                    <div class="pure-g">
                        <div class="pure-u-1-12"></div>
                        <div class="pure-u-4-5"><button id="post" class="pure-button blue-button">Save</button></div></div>
                        <input type="hidden" id="id" name="id" value="0" />
                    </div>
                    <div class="pure-g dropbtn">
                        <div class="pure-u-22-24">
                            Toggle 
                        </div>
                        <div class="pure-u-2-24">
                            <svg onclick="" xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" viewBox="0 0 24 24"><g fill="none" stroke="white" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"><path stroke-dasharray="42" stroke-dashoffset="42" d="M11 5H5V19H19V13"><animate fill="freeze" attributeName="stroke-dashoffset" dur="0.6s" values="42;0"/></path><path stroke-dasharray="12" stroke-dashoffset="12" d="M13 11L20 4"><animate fill="freeze" attributeName="stroke-dashoffset" begin="0.6s" dur="0.3s" values="12;0"/></path><path stroke-dasharray="8" stroke-dashoffset="8" d="M21 3H15M21 3V9"><animate fill="freeze" attributeName="stroke-dashoffset" begin="0.9s" dur="0.2s" values="8;0"/></path></g></svg>
                        </div>
                    </div>
                </form>
            </div>
        <script>
        function forecastList() {{
            document.getElementById("forecast").classList.toggle("show");
            document.getElementById("forecast").scrollIntoView({{ block: "center", behavior: 'smooth' }});
        }}
        </script>{default[6]}"""                                                                                                                                                                                                  
        return HTMLResponse(content=pagecontent)

@train_dev.post("/sendchat")
async def points(text: Annotated[str, Form()]):
    global chatarea

    from openai import OpenAI

    client = OpenAI()

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": text}
        ]
    )
    reply_content = response.choices[0].message.content
    chat= f"""<div class="pure-g"><div class="pure-u-10-24"></div><div class="pure-u-12-24"><p class="right">{text}</p></div><div class="pure-u-2-24"></div></div><br><div class="pure-g"><div class="pure-u-2-24"></div><div class="pure-u-12-24"><p>{reply_content}</p></div><div class="pure-u-10-24"></div></div>"""
    chatarea.append(chat)
    id=0
    for id in range(n0):
            userAnalysis(id, text)


    return {"text": text}


@train_dev.get("/user")
async def main():
        global chatarea
        pagecontent = f"""
        <!DOCTYPE html>
        <html lang="en">
          <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title></title>
            <link href="static/css/styles.css" rel="stylesheet">
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/purecss@3.0.0/build/pure-min.css" integrity="sha384-X38yfunGUhNzHpBaEBsWLO+A0HDYOQi8ufWDkZ0k9e0eXz/tH3II7uKZ9msv++Ls" crossorigin="anonymous"><lambda parameter_list: expression>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/purecss@3.0.0/build/grids-responsive-min.css">
          </head>
        <body>
           <div class="pure-g">
                <div class="pure-u-2-24"><svg xmlns="http://www.w3.org/2000/svg" width="3em" height="3em" viewBox="0 0 512 512"><path fill="none" stroke="#fcd34d" stroke-linecap="round" stroke-linejoin="round" stroke-width="15" d="m105.7 263.5l107.5 29.9a7.9 7.9 0 0 1 5.4 5.4l29.9 107.5a7.8 7.8 0 0 0 15 0l29.9-107.5a7.9 7.9 0 0 1 5.4-5.4l107.5-29.9a7.8 7.8 0 0 0 0-15l-107.5-29.9a7.9 7.9 0 0 1-5.4-5.4l-29.9-107.5a7.8 7.8 0 0 0-15 0l-29.9 107.5a7.9 7.9 0 0 1-5.4 5.4l-107.5 29.9a7.8 7.8 0 0 0 0 15Z"><animateTransform additive="sum" attributeName="transform" calcMode="spline" dur="6s" keySplines=".42, 0, .58, 1; .42, 0, .58, 1" repeatCount="indefinite" type="rotate" values="-15 256 256; 15 256 256; -15 256 256"/><animate attributeName="opacity" dur="6s" values="1; .75; 1; .75; 1; .75; 1"/></path></svg></div>
                <div class="pure-u-20-24 center"><h1>NORU</h1></div>
                <div class="pure-u-2-24"><svg xmlns="http://www.w3.org/2000/svg" width="3em" height="3em" viewBox="0 0 512 512"><defs><linearGradient id="meteoconsStarFill0" x1="187.9" x2="324.1" y1="138.1" y2="373.9" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#fcd966"/><stop offset=".5" stop-color="#fcd966"/><stop offset="1" stop-color="#fccd34"/></linearGradient></defs><path fill="url(#meteoconsStarFill0)" stroke="#fcd34d" stroke-linecap="round" stroke-linejoin="round" stroke-width="4" d="m105.7 263.5l107.5 29.9a7.9 7.9 0 0 1 5.4 5.4l29.9 107.5a7.8 7.8 0 0 0 15 0l29.9-107.5a7.9 7.9 0 0 1 5.4-5.4l107.5-29.9a7.8 7.8 0 0 0 0-15l-107.5-29.9a7.9 7.9 0 0 1-5.4-5.4l-29.9-107.5a7.8 7.8 0 0 0-15 0l-29.9 107.5a7.9 7.9 0 0 1-5.4 5.4l-107.5 29.9a7.8 7.8 0 0 0 0 15Z"><animateTransform additive="sum" attributeName="transform" calcMode="spline" dur="6s" keySplines=".42, 0, .58, 1; .42, 0, .58, 1" repeatCount="indefinite" type="rotate" values="-15 256 256; 15 256 256; -15 256 256"/><animate attributeName="opacity" dur="6s" values="1; .75; 1; .75; 1; .75; 1"/></path></svg></div>
           </div>
            {''.join(chatarea)}
           <div class="chatfooter">
                <div class="pure-g blue-button">
                    <div class="pure-u-2-24"></div>
                    <div class="pure-u-20-24">
                        <form action="/sendchat" enctype="multipart/form-data" method="post"> 
                            <input type="text" name="text" id="text" class="scorename" placeholder="New Course">
                        </form>
                    </div>
                    <div class="pure-u-2-24"></div>
                </div>
                <div class="pure-g">
                    <div class="pure-u-1-2 dropbtn">
                    <a href="/user">
                        <svg xmlns="http://www.w3.org/2000/svg" width="3em" height="3em" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"><path stroke-dasharray="68" stroke-dashoffset="68" d="M3 19.5V4C3 3.44772 3.44772 3 4 3H20C20.5523 3 21 3.44772 21 4V16C21 16.5523 20.5523 17 20 17H5.5z"><animate fill="freeze" attributeName="stroke-dashoffset" dur="0.6s" values="68;0"/></path><path stroke-dasharray="10" stroke-dashoffset="10" d="M8 7h8" opacity="0"><set attributeName="opacity" begin="0.7s" to="1"/><animate fill="freeze" attributeName="stroke-dashoffset" begin="0.7s" dur="0.2s" values="10;0"/></path><path stroke-dasharray="10" stroke-dashoffset="10" d="M8 10h8" opacity="0"><set attributeName="opacity" begin="0.8s" to="1"/><animate fill="freeze" attributeName="stroke-dashoffset" begin="0.8s" dur="0.2s" values="10;0"/></path><path stroke-dasharray="6" stroke-dashoffset="6" d="M8 13h4" opacity="0"><set attributeName="opacity" begin="0.9s" to="1"/><animate fill="freeze" attributeName="stroke-dashoffset" begin="0.9s" dur="0.2s" values="6;0"/></path></g></svg>
                    </a>
                    </div>
                    <div class="pure-u-1-2 dropbtn">
                    <a href="/training">
                        <svg xmlns="http://www.w3.org/2000/svg" width="3em" height="3em" viewBox="0 0 24 24"><g fill="currentColor"><path fill-opacity="0" stroke="currentColor" stroke-dasharray="46" stroke-dashoffset="46" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 17H9V14.1973C7.2066 13.1599 6 11.2208 6 9C6 5.68629 8.68629 3 12 3C15.3137 3 18 5.68629 18 9C18 11.2208 16.7934 13.1599 15 14.1973V17z"><animate fill="freeze" attributeName="stroke-dashoffset" dur="0.4s" values="46;0"/><animate fill="freeze" attributeName="fill-opacity" begin="0.7s" dur="0.5s" values="0;1"/></path><rect width="6" height="0" x="9" y="20" rx="1"><animate fill="freeze" attributeName="height" begin="0.5s" dur="0.2s" values="0;2"/></rect></g></svg>
                    </a>
                    </div>
                </div>
           </div>
        </body>
        </html>
        """                                                                                                                                                                                                
        return HTMLResponse(content=pagecontent)

@train_dev.get("/training")
async def main():
        global usercourses 
        pagecontent = f"""
        <!DOCTYPE html>
        <html lang="en">
          <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title></title>
            <link href="static/css/styles.css" rel="stylesheet">
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/purecss@3.0.0/build/pure-min.css" integrity="sha384-X38yfunGUhNzHpBaEBsWLO+A0HDYOQi8ufWDkZ0k9e0eXz/tH3II7uKZ9msv++Ls" crossorigin="anonymous"><lambda parameter_list: expression>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/purecss@3.0.0/build/grids-responsive-min.css">
          </head>
        <body>
           <div class="pure-g">
                <div class="pure-u-2-24"><svg xmlns="http://www.w3.org/2000/svg" width="3em" height="3em" viewBox="0 0 512 512"><path fill="none" stroke="#fcd34d" stroke-linecap="round" stroke-linejoin="round" stroke-width="15" d="m105.7 263.5l107.5 29.9a7.9 7.9 0 0 1 5.4 5.4l29.9 107.5a7.8 7.8 0 0 0 15 0l29.9-107.5a7.9 7.9 0 0 1 5.4-5.4l107.5-29.9a7.8 7.8 0 0 0 0-15l-107.5-29.9a7.9 7.9 0 0 1-5.4-5.4l-29.9-107.5a7.8 7.8 0 0 0-15 0l-29.9 107.5a7.9 7.9 0 0 1-5.4 5.4l-107.5 29.9a7.8 7.8 0 0 0 0 15Z"><animateTransform additive="sum" attributeName="transform" calcMode="spline" dur="6s" keySplines=".42, 0, .58, 1; .42, 0, .58, 1" repeatCount="indefinite" type="rotate" values="-15 256 256; 15 256 256; -15 256 256"/><animate attributeName="opacity" dur="6s" values="1; .75; 1; .75; 1; .75; 1"/></path></svg></div>
                <div class="pure-u-20-24 center"><h1>NORU</h1></div>
                <div class="pure-u-2-24"><svg xmlns="http://www.w3.org/2000/svg" width="3em" height="3em" viewBox="0 0 512 512"><defs><linearGradient id="meteoconsStarFill0" x1="187.9" x2="324.1" y1="138.1" y2="373.9" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#fcd966"/><stop offset=".5" stop-color="#fcd966"/><stop offset="1" stop-color="#fccd34"/></linearGradient></defs><path fill="url(#meteoconsStarFill0)" stroke="#fcd34d" stroke-linecap="round" stroke-linejoin="round" stroke-width="4" d="m105.7 263.5l107.5 29.9a7.9 7.9 0 0 1 5.4 5.4l29.9 107.5a7.8 7.8 0 0 0 15 0l29.9-107.5a7.9 7.9 0 0 1 5.4-5.4l107.5-29.9a7.8 7.8 0 0 0 0-15l-107.5-29.9a7.9 7.9 0 0 1-5.4-5.4l-29.9-107.5a7.8 7.8 0 0 0-15 0l-29.9 107.5a7.9 7.9 0 0 1-5.4 5.4l-107.5 29.9a7.8 7.8 0 0 0 0 15Z"><animateTransform additive="sum" attributeName="transform" calcMode="spline" dur="6s" keySplines=".42, 0, .58, 1; .42, 0, .58, 1" repeatCount="indefinite" type="rotate" values="-15 256 256; 15 256 256; -15 256 256"/><animate attributeName="opacity" dur="6s" values="1; .75; 1; .75; 1; .75; 1"/></path></svg></div>
           </div>
            {usercourses}
           <div class="chatfooter">
                <div class="pure-g">
                    <div class="pure-u-1-2 dropbtn">
                    <a href="/user">
                        <svg xmlns="http://www.w3.org/2000/svg" width="3em" height="3em" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"><path stroke-dasharray="68" stroke-dashoffset="68" d="M3 19.5V4C3 3.44772 3.44772 3 4 3H20C20.5523 3 21 3.44772 21 4V16C21 16.5523 20.5523 17 20 17H5.5z"><animate fill="freeze" attributeName="stroke-dashoffset" dur="0.6s" values="68;0"/></path><path stroke-dasharray="10" stroke-dashoffset="10" d="M8 7h8" opacity="0"><set attributeName="opacity" begin="0.7s" to="1"/><animate fill="freeze" attributeName="stroke-dashoffset" begin="0.7s" dur="0.2s" values="10;0"/></path><path stroke-dasharray="10" stroke-dashoffset="10" d="M8 10h8" opacity="0"><set attributeName="opacity" begin="0.8s" to="1"/><animate fill="freeze" attributeName="stroke-dashoffset" begin="0.8s" dur="0.2s" values="10;0"/></path><path stroke-dasharray="6" stroke-dashoffset="6" d="M8 13h4" opacity="0"><set attributeName="opacity" begin="0.9s" to="1"/><animate fill="freeze" attributeName="stroke-dashoffset" begin="0.9s" dur="0.2s" values="6;0"/></path></g></svg>
                    </a>
                    </div>
                    <div class="pure-u-1-2 dropbtn">
                    <a href="/training">
                        <svg xmlns="http://www.w3.org/2000/svg" width="3em" height="3em" viewBox="0 0 24 24"><g fill="currentColor"><path fill-opacity="0" stroke="currentColor" stroke-dasharray="46" stroke-dashoffset="46" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 17H9V14.1973C7.2066 13.1599 6 11.2208 6 9C6 5.68629 8.68629 3 12 3C15.3137 3 18 5.68629 18 9C18 11.2208 16.7934 13.1599 15 14.1973V17z"><animate fill="freeze" attributeName="stroke-dashoffset" dur="0.4s" values="46;0"/><animate fill="freeze" attributeName="fill-opacity" begin="0.7s" dur="0.5s" values="0;1"/></path><rect width="6" height="0" x="9" y="20" rx="1"><animate fill="freeze" attributeName="height" begin="0.5s" dur="0.2s" values="0;2"/></rect></g></svg>
                    </a>
                    </div>
                </div>
           </div>
        </body>
        </html>
        """                                                                                                                                                                                                
        return HTMLResponse(content=pagecontent)


