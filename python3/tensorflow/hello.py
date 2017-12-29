import tensorflow as tf

def hello():
    hello = tf.constant("Hello, TensorFlow")
    sess = tf.Session()
    print(sess.run(hello)) 
    print(hello) #a tensor , a data
    print(sess) #a session
    
def test1():
    """
    create tensor (data) node
    """
    node1 = tf.constant(3.0, dtype=tf.float32)
    node2 = tf.constant(4.0)
    print("node1,2=",node1, node2)
    
    """
    a session to evalute node
    """
    sess = tf.Session()
    result = sess.run( [node1, node2] )
    print("node result=", result)
    

    
    """
    create opration node
    """
    node3 = tf.add(node1, node2)
    print("node3=",node3)
    result = sess.run(node3)
    print("node3 result=", result)
    

def test2():
    """
    a session to evalute node
    """
    sess = tf.Session()
    
    """
    create placeholders ( a parameter to tensorflow session)
    """
    a = tf.placeholder(dtype=tf.float32)
    b = tf.placeholder(dtype=tf.float32)
    adder_node = a + b
    
    """
    Clouds:Use a "dict" to pass parameter (placeholder) 
    """
    result = sess.run(adder_node, {a:1 , b:2})
    print("result=", result)
    
    """
    more operation
    """
    add_and_triple = adder_node * 3
    result = sess.run(add_and_triple, {a:1 , b:2})
    print("result=", result)
    
def linear_regression():
    """
    linear model = W * x + b = y 
    W : each test weighting value
    x : training data , experimental data (many,many..)
    y : "standard answer/desired value" based on "training data/sampling data"
    
    ==> have a set of training data, x , find the (W,b) have the min loss
    Clouds: the dimention of W & x are eaual to the count of features  
    """
    #1. Weighting variable 
    W = tf.Variable([.3], dtype=tf.float32)
    b = tf.Variable([-.3], dtype=tf.float32)
#     W = tf.constant([.3], dtype=tf.float32)
#     b = tf.constant([-.3], dtype=tf.float32)
     
    #initial variable
    sess = tf.Session()
    init = tf.global_variables_initializer()
    sess.run(init)
    
    #2. training data
    x = tf.placeholder(tf.float32)
    y = tf.placeholder(tf.float32)


    #3.linear model equation
    linear_model = W*x + b
    
    """
    linear model test
    """
    print("linear_model = ", sess.run(linear_model, { x: [1,2,3,4] })) #.3*x -.3 = ?  (feed with each training data)
    
    """
    loss function
    """
    square_deltas = tf.square(linear_model-y)
    print("(linear_model-y)^2 = ", sess.run(square_deltas, { x: [1,2,3,4], y: [0, -1, -2, -3] }))
    
    loss = tf.reduce_sum(square_deltas) #just to sum up each element in array 
    print("loss = ", sess.run(loss, { x: [1,2,3,4], y: [0, -1, -2, -3] }))
    
#     """
#     Manualy Find the min loss value by assign W=-1 , b=1
#     """
#     #change variable value/CLS: you can't change value of constant 
#     fixW = tf.assign(W,[-1.])
#     fixb = tf.assign(b,[1.])
#      
#     print("run assign=",sess.run([fixW,fixb]))
#     
#     #run again loss function
#     print("loss2 = ", sess.run(loss, { x: [1,2,3,4], y: [0, -1, -2, -3] }))
    
    
    """
    =====================================
    tf.train API
    =====================================
    """
    optimizer = tf.train.GradientDescentOptimizer(0.01)
    print("optimizer=",optimizer)
    """
    loss = tf.reduce_sum(square_deltas) = tf.reduce_sum(tf.square(linear_model-y)) = tf.reduce_sum(tf.square(  (W*x + b) -y  ))
    Clouds: optimizer will change variables in loss(W,b), loop by loop to minimize the value of loss(W,b)
    """
    train = optimizer.minimize(loss)
    print("train=",train)
    
    """
    Train Data
    """
    x_train = [1,2,3,4]
    y_train = [0, -1, -2, -3]
    
    """
    Run Train
    Clouds: each loop of optimizer function "train", optimizer framework will "change variable (by tf.assign)" and find the minimal loss value 
    """
    sess.run(init) # reset values to incorrect defaults.
    for i in range(2000):
        print(i)
        print("run train=", sess.run(train, { x: x_train, y: y_train }))
        print("[W, b]=", sess.run([W, b]))
        
        
    """
    After change variables in loss, we got (W,b) produce the minimized loss value 
    """
    print("minimized [W, b, loss]=", sess.run([W, b, loss], { x: x_train, y: y_train }) )
    
    
    
    
    
    
    
    
def mytest():
    """
    a session to evalute node
    """
    sess = tf.Session()
    
    """
    create tensor (data) node
    """
    node1 = tf.constant([3.0,2.0], dtype=tf.float32)
    node2 = tf.constant([4.0,3.0])
    
#     node1 = tf.Variable([3.0,2.0], dtype=tf.float32)
#     node2 = tf.Variable([4.0,3.0], dtype=tf.float32)
#     init = tf.global_variables_initializer()
#     sess.run(init)
    

    
    """
    create opration node
    """
    node3 = node1 + node2
    
    """
    placeholder
    """
    a = tf.placeholder(dtype=tf.float32)
    
    """
    model
    """
#     model = node3*a
    model = (node1 + node2)*a


    
    result = sess.run( model, {a:[1,2]} )
    print("result=", result)
    
    
    
    
    
    
    
if __name__ == '__main__':
#     hello()
#     test1()
#     test2() #placeholder test
#     mytest()
    linear_regression()
    
    print("Done!")
    pass