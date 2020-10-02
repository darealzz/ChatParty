from flask import Flask, render_template
import asyncpg
import asyncio


# -- SCOPES -- #
#soc = socketio.Client()
app = Flask(__name__)


@app.route("/home")
@app.route("/")
def index():
    return render_template('index.html', PageName='Home')


# -- DATABASE CONNECTIONS -- #
async def create_db_pool():
    try:
        pg_con = await asyncpg.create_pool(host='192.168.1.156', database="ChatParty", user="postgres", password='68fDx@"Z4~BHa9X<')
    except asyncpg.exceptions.InvalidAuthorizationSpecificationError:
        pg_con = await asyncpg.create_pool(host='localhost', database="ChatParty", user="postgres", password='68fDx@"Z4~BHa9X<')
    print('log line')


# -- SOCKET -- # 
#@soc.event
#def connect(): 
 # print('[SOC] Connection Enstablished.')

#@soc.event 
#def disconnect(): 
    #print('[SOC] Connection Terminated.')

 #soc.connect('http://127.0.0.1:5000')
 #soc.wait()

if __name__ == '__main__': 
    app.run(debug=False)

    ## -- ASYNCIO -- #

    loop = asyncio.get_event_loop()
    loop.run_until_complete(create_db_pool())
    loop.close()
