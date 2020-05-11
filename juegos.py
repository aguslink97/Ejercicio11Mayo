import hangman
import reversegam
import tictactoeModificado
import PySimpleGUI as sg
from funcionjugadores import menujugador


layout = [
    		 [sg.Text('Elegí con qué juego querés jugar:	1.- Ahorcado 2.- Ta-TE-TI 3.- Otello 4.- Salir'),sg.Input(key='_numero_')],
  			 [sg.Button('cargar')]
	 ]
window = sg.Window('menu del juego').Layout(layout)
event,values = window.Read()
if values['_numero_'] == '':
     sg.Popup('Falta completar algun campo') 

def menu():
 sigo_jugando=True
 while sigo_jugando:
	 if not(values['_numero_']=='4'):
	     if (values['_numero_']=='1'):
   		     hangman.main()  
 	     if (values['_numero_']=='2'):
   		 	 tictactoeModificado.main()
	     elif (values['_numero_']=='3'):
        	 reversegam.main()
	 else:
    	 sigo_jugando = False

menu()