import numpy as np
import configparser

# Esta clase es el experimento. Sus atributos son los parámetros de la simulación y los datos que genera.
# sus métodos son crear un archivo de configuración, correr la simulación y guardar los datos generados

class experimento():
    def __init__(self, nGotas=10, nLotes=10, saturacion=15, nDim=10):# , *args):
        self.nGotas = nGotas
        self.nLotes = nLotes
        self.saturacion = saturacion
        self.grilla = np.zeros([nDim])#np.zeros([args])
        self.datos = np.zeros([nLotes,nDim])#([args, nLotes])

    def EscribirDatos(self, nombreArchivo):
        """
        Esta función escribe el archivo de configuración y los datos asociados a cada corrida de la simulación
        """
        # los archivos de datos y de configuración se llaman igual con distinta extensión
        np.savetxt('{}.data'.format(nombreArchivo), self.datos, delimiter=',')

        mFilas, nColumnas = self.datos.shape
        print(self.datos.shape)

        config = configparser.RawConfigParser()
        nombreSeccion = 'configuracion'
        config.add_section(nombreSeccion)
        config.set(nombreSeccion, 'Num de gotas', '{}'.format(self.nGotas))
        config.set(nombreSeccion, 'Num de lotes', '{}'.format(self.nLotes))
        config.set(nombreSeccion, 'Saturacion', '{}'.format(self.saturacion))
        config.set(nombreSeccion, 'Tam de la grilla', '{}'.format(len(self.grilla)))
        config.set(nombreSeccion, 'archivo con datos', '{}'.format(nombreArchivo))
        config.set(nombreSeccion, 'Num filas', '{}'.format(mFilas))
        config.set(nombreSeccion, 'Num columnas', '{}'.format(nColumnas))
        # Writing our configuration file to 'example.cfg'
        with open('{}.cfg'.format(nombreArchivo), 'w') as configfile:
            config.write(configfile)

    def Correr(self):
        contadorFilas = 0
        for iLot in range(self.nLotes):
            # para el número indicado de lotes
            for iGot in range(self.nGotas):
                self.grilla[np.random.randint(0, len(self.grilla))] +=1
            #print(self.grilla)
            self.datos[iLot,:] = self.grilla
            
            if self.grilla.min() >=self.saturacion:
                break           # la simulacion debe detenerse cuando cada espacio ha alcanzado la saturacion
            else: 
                contadorFilas += 1
        nuevo_datos = np.array([self.datos[iFila,:] for iFila in range(contadorFilas)])
        nuevo_datos[nuevo_datos > self.saturacion] = self.saturacion
        self.datos = nuevo_datos
        #print(contadorFilas)
