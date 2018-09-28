import numpy as np

if __name__ == '__main__':
    import experimento, visualizacion

    prueba = experimento.experimento(10, 10, 15, 5)
    prueba.Correr()
    prueba.EscribirDatos('prueba')
    plot = visualizacion.PlotEnv('prueba')

    with open('prueba.data', 'r') as dataFile:
        dato = np.loadtxt(dataFile, delimiter=',')

#    m,n = np.shape(dato)

#    for iFila in range(n):
    plot.ActualizarVis(dato)