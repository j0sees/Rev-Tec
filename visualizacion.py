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
        nDim = run_config.getint(nombreSeccion, 'Tam de la grilla')
        nLot = run_config.getint(nombreSeccion, 'Num de lotes')
        saturacion = run_config.getint(nombreSeccion, 'Saturacion')

        ##################################################
        # Luego se crea la figura
        ##################################################
        plt.close()
        self.Figura, self.grilla = plt.subplots(1,1)

        pad_dist = 0.01
        shrink_pct = 1

        self.Figura.suptitle('Visualización de las gotas sobre la grilla', fontweight='bold')
        self.vector = np.zeros([nLot,nDim])
        self.Plot = self.grilla.imshow(self.vector, origin='upper', cmap='Blues', interpolation='none', vmin=0,vmax=saturacion)
        cbar1 = self.Figura.colorbar(self.Plot, ax=self.grilla, ticks=[], orientation='vertical',pad=pad_dist, shrink=shrink_pct)

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
