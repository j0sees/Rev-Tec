#import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import configparser

class PlotEnv:
    def __init__(self, nombreArchivo):

        ##################################################
        # Primero se lee el archivo de configuración
        ##################################################
        run_config = configparser.RawConfigParser()
        run_config.read('{}.cfg'.format(nombreArchivo))

        nombreSeccion = 'configuracion'
        mFil = run_config.getint(nombreSeccion, 'Num filas')
        nCol = run_config.getint(nombreSeccion, 'Num columnas')
        self.saturacion = run_config.getint(nombreSeccion, 'Saturacion')

        ##################################################
        # Luego se crea la figura
        ##################################################
        plt.close()
        self.Figura, self.grilla = plt.subplots(1,1)

        pad_dist = 0.01
        shrink_pct = 1

        self.Figura.suptitle('Visualización de las gotas sobre la grilla', fontweight='bold')
        self.vector = np.zeros([mFil, nCol])
        self.Plot = self.grilla.imshow(self.vector, origin='upper', cmap='Blues', interpolation='none', vmin=0, vmax=self.saturacion)
        cbar1 = self.Figura.colorbar(self.Plot, ax=self.grilla, ticks=[], orientation='vertical', pad=pad_dist, shrink=shrink_pct)

        plt.ion()
        #plt.pause(0.001)
        self.Figura.canvas.draw()
        plt.ioff()

    def ActualizarVis(self, datos):
        #
        self.Plot.set_data(datos)
        #
        self.grilla.draw_artist(self.grilla.patch)
        self.grilla.draw_artist(self.Plot)

#        plt.savefig('best_unique_genome_{0}/cell_system-{1:03d}.png'.format(iGenome + 1, tStep, ), format='png',bbox_inches='tight')
        plt.show()

    def HistogramaColor(self, datos):
        plt.close()
        bins=[ix for ix in range(self.saturacion)]# + 1)]
        hist, bins = np.histogram(datos, bins=bins)
        print(hist)
        
        width = 0.7 * (bins[1] - bins[0])
        center = (bins[:-1] + bins[1:]) / 2
        plt.bar(center, hist, align='center', width=width)
        
        #plt.hist(histograma, bins=bins)
        plt.show()
    # contar cuantas celdas tienen uns unidad, cuantas tienen 2, etc...
    # hacer un histograma para cada categoría de color despues de cierta cantidad de lotes.

    #def HistogramaSTD(self):

    # calcular el promedio de la distribucion para cada grupo de lotes y su desviación estándar.
