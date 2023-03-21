import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import xarray as xr


# ax = plt.axes(projection=ccrs.Mollweide())
# ax.stock_img()
# plt.show()

dset = xr.open_dataset("es ")

dset['tp'].plot()

dset['tp'].plot(cmap='jet', vmax=0.02)


fig2 = plt.figure(figsize=[12,5])

# 111 means 1 row, 1 col and index 1
ax2 = fig2.add_subplot(111, projection=ccrs.PlateCarree(central_longitude=0))

dset['tp'].plot(ax=ax2, vmax=0.02, cmap='jet',
                   transform=ccrs.PlateCarree())
ax2.coastlines()

plt.show()


fig3 = plt.figure(figsize=[12,5])

# 111 means 1 row, 1 col and index 1
ax3 = fig3.add_subplot(111, projection = ccrs.Orthographic(central_longitude=20, central_latitude=40))

dset['t2m'].plot(ax=ax3,  cmap='jet',
                   transform=ccrs.PlateCarree())
ax3.coastlines()

plt.show()