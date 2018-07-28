import bpy


def write_some_data(context, filepath, shift):
    print("running write_some_data...")
    
    
    selection = bpy.context.selected_objects
    bpy.ops.object.select_all(action='DESELECT')
#    activename = bpy.path.clean_name(bpy.context.scene.objects.active.name)
#    fn = os.path.join(basedir, activename)
    
    
    f = open(filepath, 'w', encoding='utf-8')
        
#    file = open(fn + ".txt", 'w')

    # write selected objects coordinate
    for obj in selection:
        obj.select = True

        x_coor = obj.location[0]
        y_coor = obj.location[1]
        z_coor = obj.location[2]
            
        if shift == True:
            shift_x = context.scene.BL_x_shift
            shift_y = context.scene.BL_y_shift
            shift_z = context.scene.BL_z_shift
            x_coor = x_coor-shift_x
            y_coor = y_coor-shift_y
            z_coor = z_coor-shift_z  

        # Generate UV sphere at x = lon and y = lat (and z = 0 )
    
        f.write("%s %s %s %s\n" % (obj.name, x_coor, y_coor, z_coor))
    f.close()    
    

#    f.write("Hello World %s" % use_some_setting)
#    f.close()

    return {'FINISHED'}


# ExportHelper is a helper class, defines filename and
# invoke() function which calls the file selector.
from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator


class ExportSomeData(Operator, ExportHelper):
    """This appears in the tooltip of the operator and in the generated docs"""
    bl_idname = "export_test.some_data"  # important since its how bpy.ops.import_test.some_data is constructed
    bl_label = "Export Some Data"

    # ExportHelper mixin class uses this
    filename_ext = ".txt"

    filter_glob = StringProperty(
            default="*.txt",
            options={'HIDDEN'},
            maxlen=255,  # Max internal buffer length, longer would be clamped.
            )

    # List of operator properties, the attributes will be assigned
    # to the class instance from the operator settings before calling.

    shift = BoolProperty(
            name="Shift coordinates",
            description="Shift coordinates using the General Shift Value (GSV)",
            default=False,
            )


    def execute(self, context):
        return write_some_data(context, self.filepath, self.shift)


# Only needed if you want to add into a dynamic menu
def menu_func_export(self, context):
    self.layout.operator(ExportSomeData.bl_idname, text="Text Export Operator")


#def register():
#    bpy.utils.register_class(ExportSomeData)
#    bpy.types.INFO_MT_file_export.append(menu_func_export)


#def unregister():
#    bpy.utils.unregister_class(ExportSomeData)
#    bpy.types.INFO_MT_file_export.remove(menu_func_export)


#if __name__ == "__main__":
#    register()

#    # test call
#    bpy.ops.export_test.some_data('INVOKE_DEFAULT')
