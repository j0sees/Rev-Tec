import numpy as np

if __name__ == '__main__':
    import experimento, visualizacion

#                                   nGotas, nLotes, saturacion, nDim
    prueba = experimento.experimento(1000,    100,     15,         1000)
    prueba.Correr()
    prueba.EscribirDatos('prueba')
    plot = visualizacion.PlotEnv('prueba')

    with open('prueba.data', 'r') as dataFile:
        dato = np.loadtxt(dataFile, delimiter=',')
    print(dato)

#    plot.ActualizarVis(dato)
    plot.HistogramaColor(dato)
