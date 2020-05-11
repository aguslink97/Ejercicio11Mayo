import PySimpleGUI as sg
import json

#la estructura de datos es diccionario para guardar el nombre,apellido y a que juego jugo
#me decidi por los archivos JSON  ya que es mucho más fácil y siempre  porque le permite abrirlo en un editor de texto y revisar los datos 

jug={}


def guardarjugadores(jug):
    with open('jugadores.json','w') as archivo:
        json.dump(jug,archivo)
       
def leerjugadores ():
    with open('jugadores.json','r') as archivo:
        jug=json.load(archivo)
    return jug

def nombrejuego(numero):
    if(numero==1):
        juego='Ahorcado';
    elif(numero==2):
        juego='TaTeTi';
    else:
        juego='Otello';

def cargarjugador(values,num):
    leerjugadores();
    nombre=str(values['_nombre_']).lower()
    juego=nombrejuego(num)
    jug[nombre] = {
                   ' apellido ': str(values['_apellido_']).lower(),
                   ' el jugador juego al ': juego 
                  }   
    guardarjugadores(jug)


# Definir el layout
layout = [
    [sg.Text('nombre del jugador'),sg.Input(key='_nombre_')],
    [sg.Text('apellido del jugador'),sg.Input(key='_apellido_')],    
    [sg.Button('cargar')]
]

window = sg.Window('programa juego').Layout(layout)

def menujugador(numero):
  event, values = window.Read()
  if values['_nombre_'] == '' or values['_apellido_']=='' :
     sg.Popup('Falta completar algun campo') 
  else:
     cargarjugador(values,numero)
     print(leerjugadores())
