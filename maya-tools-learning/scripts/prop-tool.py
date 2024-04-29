from maya import cmds

prop_type = 'Sphere'

ctrl_var = 'control'
prop_var = 'prop'

ctrl = cmds.circle(name = ctrl_var,r=2,nr = [0,1,0])
ctrl_node = ctrl[0]

if prop_type == 'Sphere':
    prop = cmds.polySphere(name = prop_var)

elif prop_type == 'Cube':
    prop = cmds.polyCube(name = prop_var)
    
prop_node = prop[0]
   



cmds.parent(prop_node,ctrl_node)