from fanstatic import Group
from fanstatic import Library
from fanstatic import Resource

from js.jquery import jquery

library = Library('gridster', 'resources')

jquery_gridster_css = Resource(library,
                               "jquery.gridster.css",
                               minified="jquery.gridster.min.css")
jquery_collision = Resource(library, "jquery.collision.js",
                            minified="jquery.collision.min.js")
jquery_coords = Resource(library, "jquery.coords.js",
                         minified="jquery.coords.min.js")
jquery_draggable = Resource(library, "jquery.draggable.js",
                            minified="jquery.draggable.min.js")
jquery_gridster_extras = Resource(library,
                                  "jquery.gridster.extras.js",
                                  minified="jquery.gridster.extras.min.js")
jquery_gridster_utils = Resource(library,
                                 "utils.js",
                                 minified='utils.min.js')
jquery_gridster = Resource(library, "jquery.gridster.js",
                           minified='jquery.gridster.min.js',
                           depends=[jquery,
                                    jquery_collision,
                                    jquery_coords,
                                    jquery_draggable,
                                    #jquery_gridster_extras,
                                    jquery_gridster_utils])

gridster = Group([jquery_gridster_css, jquery_gridster])
