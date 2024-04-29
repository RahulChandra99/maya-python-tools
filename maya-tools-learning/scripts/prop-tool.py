from maya import cmds


def create_prop_rig(propToMake):
    """
    Create a piece of geo with a control in it
    
    Args:
        prop_type(str):cube or sphere
        
        Return:
            ctrl_node(str): name of control node
    """
    ctrl_var = 'control'
    prop_var = 'prop'

    ctrl = cmds.circle(name = ctrl_var,r=2,nr = [0,1,0])
    ctrl_node = ctrl[0]
    prop_type = propToMake
    if prop_type == 'Sphere':
        prop = cmds.polySphere(name = prop_var)
    elif prop_type == 'Cube':
        prop = cmds.polyCube(name = prop_var)
    
    prop_node = prop[0]
    
    # parent prop to control node
    cmds.parent(prop_node,ctrl_node)
    
    return ctrl_node
   
tool = create_prop_rig('Sphere')
cmds.move(-5,0,0,tool)
create_prop_rig('Cube')


