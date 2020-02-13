##########################
##
## ART SCRIPTING PART 1
##
#########################

init python:
    # Define layer ordering from back to front
    layerorder = ['hair', 'base', 'arms', 'tail','mouth','eyes','brow',]

    # Automatically create a layered sprite
    DefineImages('images/sprites', composite=True, overrideLayerOrder=layerorder, offsets=(0.5, 1.0))

    MapEmote('le speaking a1', 'le neutral base arms_default mdo_default ed_default brow_default')
    MapEmote('le speaking a2', 'le neutral base arms_raised mdo_default ed_default brow_default')
    MapEmote('le frustrated a1', 'le angry base arms_default mdo_default ed_default brow_default')
    MapEmote('le frustrated a2', 'le angry base arms_raised mdo_default ed_default brow_default')
