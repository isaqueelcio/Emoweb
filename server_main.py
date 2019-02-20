# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Reflects the requests from HTTP methods GET, POST, PUT, and DELETE
# Written by Nathan Hamiel (2010)

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from optparse import OptionParser
from NeuroPy import NeuroPy
import serial
import time
import requests
from mysql import connector
import datetime
from time import sleep
import threading



########################################################


def send_datas(datas_user,signals):
    API_BASE = "https://api.myjson.com/"
    # TODO: Aqui os dados serão enviados para serem salvos no banco
    print("DADOS ENVIADOS",signals)
    return True


########################################################
neuropy = NeuroPy("COM4")  # type: NeuroPy
neuropy.start()
print("start neuro")
porta = 'COM6'
velocidade = 9600

conexao = serial.Serial(porta, velocidade);

def start_capture(datas_user,start_time,movie_name,session_id):
    print("teste")

    #datas_user = str(datas_user)
    #datas_user = datas_user.replace("['", "")
    #datas_user = datas_user.replace("']", "")




    cont = 0
    ecg = " "
    gsr = " "
    while True:
        #sleep(1)
        cont = cont + 1

        horas =  datetime.datetime.now().strftime("%H:%M:%S.%f")
        #horas = time.strftime('%H:%M:%S')
        #current_time = datetime.datetime().now()
        leitura1 = conexao.readline()
        #leitura2 = conexao.readline()

        if 'GSR' in leitura1:
            gsr = leitura1

        else:
            ecg = leitura1


        #send_datas(datas_user,neuropy.attention)

        print(horas,
              cont,
              movie_name,
              session_id,
              start_time,
              datas_user,
              neuropy.attention,
              neuropy.meditation,
              neuropy.rawValue,
              neuropy.delta,
              neuropy.theta,
              neuropy.lowAlpha,
              neuropy.highAlpha,
              neuropy.lowBeta,
              neuropy.highBeta,
              neuropy.lowGamma,
              neuropy.midGamma,
              neuropy.poorSignal,
              neuropy.blinkStrength,
              gsr,
              ecg)

        #print("User", datas_user)
        #print("Start time", start_time)
        #print("Movie", movie_name)
        #print("sessio", session_id)


        # comentar
        #horas
        #cont
        ID_filmes = movie_name
        ID_sessao = session_id
        ID_usuario = datas_user
        attention = neuropy.attention
        meditation = neuropy.meditation
        rawValue = neuropy.rawValue
        theta = neuropy.theta
        delta = neuropy.delta
        lowAlpha = neuropy.lowAlpha
        highAlpha = neuropy.highAlpha
        lowBeta = neuropy.lowBeta
        highBeta = neuropy.highBeta
        lowGamma = neuropy.lowGamma
        midGamma = neuropy.midGamma
        poorSignal = neuropy.poorSignal
        blinkStrength = neuropy.blinkStrength


        #dados = (horas, cont, ID_filmes, ID_sessao, ID_usuario, attention, meditation, rawValue, theta, delta, lowAlpha, highAlpha, lowBeta, highBeta, lowGamma, midGamma, poorSignal, blinkStrength, gsr, ecg)
        dados1 = (('horas', horas), ('cont', cont), ('ID_filmes', ID_filmes), ('ID_sessao', ID_sessao), ('ID_usuario', ID_usuario),
                 ('attention', attention), ('meditation', meditation), ('rawValue', rawValue), ('theta', theta), ('delta', delta),
                 ('lowAlpha', lowAlpha), ('highAlpha', highAlpha), ('highBeta', highBeta), ('lowBeta', lowBeta),
                 ('lowGamma', lowGamma), ('midGamma', midGamma), ('poorSignal', poorSignal), ('blinkStrength', blinkStrength),
                 ('gsr', gsr), ('ecg', ecg))

        r = requests.post('http://localhost/sensores/cad.php', data=dados1)
        print(r.text)

        #con = connector.Connect(user='root', password='', database='emobd10', host='localhost')

        #cur = con.cursor()
        '''
        sql = 'insert into dados_sensores (horas, cont, ID_filmes, ID_sessao, ID_usuario, attention, meditation, rawValue, theta, delta,' \
              'lowAlpha, highAlpha, lowBeta, highBeta, lowGamma, midGamma, poorSignal, blinkStrength, gsr, ecg) values (%s, %s, %s, %s, %s, %s, %s, %s' \
              ', %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        '''
        # cur.execute("""insert into pessoa (Nome, Sobrenome, Idade, Profissao) values (Nome, Sobrenome, Idade, Profissao);""")
        #cur.execute(sql, dados)
        #con.commit()
        #con.close()

        #comentar ate aqui

      #  cnx = mysql.connector.connect(user='root',
                                    #  host='localhost',
                                     # database='emmoweb')
       # cursor = cnx.cursor()

        #cursor.execute("INSERT INTO sensors (id, user_id, movie_name, start_time, session_id, attention, meditation, rawValue, delta, theta, lowAlpha, highAlpha, lowBeta, highBeta, lowGamma, midGamma, poorSignal, blinkStrength, gsr, ecg) VALUES ('3', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1')")
       # cursor.execute('INSERT INTO TABELA (CAMPO1, CAMPO2, CAMPO3) VALUES (?,?,?)', (valor1, valor2, valor3))

       # cnx.close()





       # requests.get('192.168.0.5:3000/sensors/v1')
      # print("teste", datas_send)

########################################################
class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        #request_path = self.path

        #print("\n----- Request Start ----->\n")
        #print(request_path)
        #print(self.headers)
        #print("<----- Request End -----\n")

        self.send_response(200)
        self.send_header("Set-Cookie", "foo=bar")

    def do_POST(self):
        request_path = self.path

        print("\n----- Request Start ----->\n")
        print(request_path)

        request_headers = self.headers
        content_length = request_headers.getheaders('content-length')



        ######################################################
        user = request_headers.getheaders('user')
        start_time = request_headers.getheaders('start_time')
        movie_name = request_headers.getheaders('movie_name')
        session_id = request_headers.getheaders('session_id')

        user = str(user)
        user =  user.replace("['", "")
        user = user.replace("']", "")

        start_time = str(start_time)
        start_time = start_time.replace("['", "")
        start_time = start_time.replace("']", "")

        movie_name = str(movie_name)
        movie_name = movie_name.replace("['", "")
        movie_name = movie_name.replace("']", "")

        session_id = str(session_id)
        session_id = session_id.replace("['", "")
        session_id = session_id.replace("']", "")


        start_capture(user, start_time, movie_name, session_id)
        #requests.get('192.168.0.5:3000/sensors/v1')





        ######################################################



        length = int(content_length[0]) if content_length else 0

        #print(request_headers)
        #print(user)
        #print(self.rfile.read(length))

        print("<----- Request End -----\n")

        self.send_response(200)
    do_PUT = do_POST
    do_DELETE = do_GET

def main():
    port = 8080
    print('Listening on localhost:%s' % port)
    server = HTTPServer(('', port), RequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    parser = OptionParser()
    parser.usage = ("Creates an http-server that will echo out any GET or POST parameters\n"
                    "Run:\n\n"
                    "   reflect")
    (options, args) = parser.parse_args()

    main()