import iris
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings(action='ignore')
import iris.coord_categorisation
import cartopy.feature as cfeature
import cartopy.crs as ccrs
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
from matplotlib import colors
import iris.plot as iplt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np
import cmocean
from iris.analysis.cartography import cosine_latitude_weights
from matplotlib.font_manager import FontProperties

s_1=iris.load_cube('/home/oppl/jis/plotwork/KORA/plotwork/ssh/data/aviso_11_21_y.nc')
s_2=iris.load_cube('/home/oppl/jis/plotwork/KORA/plotwork/ssh/data/kora_ssh_11_21_y.nc')+0.3843
s_3=iris.load_cube('/home/oppl/jis/plotwork/KORA/plotwork/ssh/data/hycom_ssh_11_21_y.nc')+0.3738
s_4=iris.load_cube('/home/oppl/jis/plotwork/KORA/plotwork/ssh/data/cmems_ssh_11_21_y.nc')+0.3920
s_5=iris.load_cube('/home/oppl/jis/plotwork/KORA/plotwork/ssh/data/bran_ssh_11_21_y.nc')+0.4244


for i in range(1,13):
    if i==12 :
        locals()['a_{0}'.format(i)]=s_1[i-2]
        locals()['b_{0}'.format(i)]=s_2[i-2]
        locals()['c_{0}'.format(i)]=s_3[i-2]
        locals()['d_{0}'.format(i)]=s_4[i-2]
        locals()['e_{0}'.format(i)]=s_5[i-2]

    else:
        locals()['a_{0}'.format(i)]=s_1[i-1]
        locals()['b_{0}'.format(i)]=s_2[i-1]
        locals()['c_{0}'.format(i)]=s_3[i-1]
        locals()['d_{0}'.format(i)]=s_4[i-1]
        locals()['e_{0}'.format(i)]=s_5[i-1]


#weights=cosine_latitude_weights(s_1)

mon=np.arange(1,13,1)

lon=s_1.coord(axis='X').points
lat=s_1.coord(axis='Y').points

lev=np.arange(1.12,1.20,0.10)
fig = plt.figure(figsize=(12,8))
fig.subplots_adjust(hspace=0.3)
lon_formatter = LongitudeFormatter()
lat_formatter = LatitudeFormatter()
proj = ccrs.PlateCarree()
ticks=np.arange(-1.1,1.3,0.2)
cmapt=plt.cm.bwr
columns=3
rows=3
#fig.subplots_adjust(wspace=0.3)

labels=['AVISO','K-ORA22','HYCOM','GLORYS','BRAN']

def plotmap(ssh1, ssh2, ssh3, ssh4, ssh5, axs):
    con1=iplt.contour(ssh1, lev, colors='black', linewidth=3)
    con2=iplt.contour(ssh2, lev, colors='red', linewidth=3)
    con3=iplt.contour(ssh3, lev, colors='blue', linewidth=3)
    con4=iplt.contour(ssh4, lev, colors='green', linewidth=3)
    con5=iplt.contour(ssh5, lev, colors='orange', linewidth=3)
  
    axs.set_extent([126,144,28,38])
    axs.xaxis.set_major_formatter(lon_formatter)
    axs.yaxis.set_major_formatter(lat_formatter)
    axs.add_feature(cfeature.NaturalEarthFeature('physical','land', '50m', facecolor = 'silver'))
    g=axs.gridlines(crs=ccrs.PlateCarree(), xlocs=range(126,144,2), ylocs=range(26,38,3), draw_labels=True, color='gray', linestyle = '--', linewidth=0.5)
    g.top_labels=False
    g.right_labels=False

    return con1,con2,con3,con4,con5

xlabel=[]

for i in range(2011,2020):
    xlabel.append(str(i)+' yr')

#xlabel=['Jan','Feb','Mar','Apr','May','Jun','Jul','Agu','Sep','Oct','Nov','Dec']

#xlabel=['(a)','(b)','(c)','(d)','(e)','(f)','(g)','(h)','(i)','(j)','(k)','(l)']

fontP = FontProperties()
fontP.set_size('large')

for i in range(1,columns*rows +1):
    locals()['ax{0}'.format(i)] = fig.add_subplot(rows, columns, i, projection=proj)
    con1,con2,con3,con4,con5=plotmap(locals()['a_{0}'.format(i)], locals()['b_{0}'.format(i)], locals()['c_{0}'.format(i)], locals()['d_{0}'.format(i)], locals()['e_{0}'.format(i)],locals()['ax{0}'.format(i)])
    locals()['ax{0}'.format(i)].set_title(xlabel[i-1], fontsize=10)
    if i==3:
        con1.collections[0].set_label(labels[0])
        con2.collections[0].set_label(labels[1])
        con3.collections[0].set_label(labels[2])
        con4.collections[0].set_label(labels[3])
        con5.collections[0].set_label(labels[4])
        ax3.legend(bbox_to_anchor=(1.02, 1), loc='upper left' ,prop=fontP) # frameon=False 

bottom, top = 0.1, 0.9

#ax12.set_visible(False)

axlist=[]
for i in range(1,10):
    axlist.append(locals()['ax{0}'.format(i)])
    locals()['ax{0}'.format(i)].text(132.5, 30, "RMSE : ", fontweight='bold', fontsize=9, transform=ccrs.PlateCarree())

ax1.text(136.2, 30.0, "K=0.62, H=1.24,", fontsize=9,transform=ccrs.PlateCarree())
ax1.text(136.2, 29.2, "G=0.53, B=0.80", fontsize=9,transform=ccrs.PlateCarree())

ax2.text(136.2, 30.0, "K=0.56, H=1.24,", fontsize=9,transform=ccrs.PlateCarree())
ax2.text(136.2, 29.2, "G=0.62, B=0.98", fontsize=9,transform=ccrs.PlateCarree())

ax3.text(136.2, 30.0, "K=0.46, H=5.37,", fontsize=9,transform=ccrs.PlateCarree())
ax3.text(136.2, 29.2, "G=1.08, B=0.45", fontsize=9,transform=ccrs.PlateCarree())

ax4.text(136.2, 30.0, "K=0.33, H=1.56,", fontsize=9,transform=ccrs.PlateCarree())
ax4.text(136.2, 29.2, "G=0.79, B=0.68", fontsize=9,transform=ccrs.PlateCarree())

ax5.text(136.2, 30.0, "K=0.65, H=1.12,", fontsize=9,transform=ccrs.PlateCarree())
ax5.text(136.2, 29.2, "G=0.44, B=0.67", fontsize=9,transform=ccrs.PlateCarree())

ax6.text(136.2, 30.0, "K=0.62, ", fontsize=9,transform=ccrs.PlateCarree())
ax6.text(136.2, 29.2, "G=0.42, B=0.55", fontsize=9,transform=ccrs.PlateCarree())

ax7.text(136.2, 30.0, "K=1.08, ", fontsize=9,transform=ccrs.PlateCarree())
ax7.text(136.2, 29.2, "G=0.59, B=0.83", fontsize=9,transform=ccrs.PlateCarree())

ax8.text(136.2, 30.0, "K=0.54, ", fontsize=9,transform=ccrs.PlateCarree())
ax8.text(136.2, 29.2, "G=0.58, B=0.71", fontsize=9,transform=ccrs.PlateCarree())

ax9.text(136.2, 30.0, "K=0.60, ", fontsize=9,transform=ccrs.PlateCarree())
ax9.text(136.2, 29.2, "G=0.51, B=1.07", fontsize=9,transform=ccrs.PlateCarree())


plt.savefig('ke_line.png', bbox_inches='tight')

plt.show()
