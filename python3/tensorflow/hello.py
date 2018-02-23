import tensorflow as tf
import numpy as np

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
    
    
    
    
    
def linear_regression_tf_estimator():
    """
    Step0: Prepare  data
    """
    """
    Clouds: 1-D feature, named "x"
    """
    feature_columns = [tf.feature_column.numeric_column("x", shape=[1])]
    
    print("feature_column =", feature_columns)
    
   
    
    
    """
    prepare tensorflow data from numpy
    Clouds: what is  batch_size? num_epochs? shuffle????
    """
    x_train = np.array([1., 2., 3., 4.])
    y_train = np.array([0., -1., -2., -3.])
    x_eval = np.array([2., 5., 8., 1.])
    y_eval = np.array([-1.01, -4.1, -7, 0.])
    input_fn = tf.estimator.inputs.numpy_input_fn(
        {"x": x_train}, y_train, batch_size=4, num_epochs=None, shuffle=True)
    train_input_fn = tf.estimator.inputs.numpy_input_fn(
        {"x": x_train}, y_train, batch_size=4, num_epochs=1000, shuffle=False)
    
    eval_input_fn = tf.estimator.inputs.numpy_input_fn(
        {"x": x_eval}, y_eval, batch_size=4, num_epochs=1000, shuffle=False)
    
    print("input_fn=",input_fn)
    print("train_input_fn=",train_input_fn)
    print("eval_input_fn=",eval_input_fn)
    
    
    
    """
    Step 1: create a estimator with 1-d feature named "x"
        Clouds:
            decide your training model (linear regression)
            feed estimator "only the features" , it will automatically decide the dimention of W and b, this is reasonable
    """
    """
    Clouds: Use default "LinearRegression" estimator
    """
    estimator = tf.estimator.LinearRegressor(feature_columns = feature_columns)
    """
    Clouds: Use customize model
    """
    estimator = tf.estimator.Estimator(model_fn=_model_fn)
    
    
    
    """
    Step2: "Training" with input_fn
        Clouds: 
            input_fn has 
                1. sample features (named x) 
                2. result (y)
            this step really do 1000 times fitting!!
    """
    # We can invoke 1000 training steps by invoking the  method and passing the
    # training data set.
    result = estimator.train(input_fn=input_fn, steps=1000)
    print("estimator.train result=", result)
    """
    Clouds: how to get the weighting value???
    """
    
    """
    Step3: "Evaluate"
        Clouds:
            Just appy the result of fitting
            evalute return:
                train metrics: {'loss': 3.5809224e-09, 'average_loss': 8.9523061e-10, 'global_step': 1000}
                it has default loss function, but what is average_loss?
                where is the weighting value?
                
    """
    # Here we evaluate how well our model did.
    train_metrics = estimator.evaluate(input_fn=train_input_fn)
    eval_metrics = estimator.evaluate(input_fn=eval_input_fn)
    print("train metrics: %r"% train_metrics)
    print("eval metrics: %r"% eval_metrics)
     
    
def _model_fn(features, labels, mode):
    print("\t_model_fn:features=", features)
    print("\t_model_fn:labels=", labels)
    print("\t_model_fn:mode=", mode)
    
    # Build a linear model and predict values
    W = tf.get_variable("W", [1], dtype=tf.float64)
    b = tf.get_variable("b", [1], dtype=tf.float64)
    y = W*features['x'] + b
    # Loss sub-graph
    """Clouds: what is "labels"? "labels" is the standard answer? where "y" is the predict answer?""" 
    loss = tf.reduce_sum(tf.square(y - labels))
    # Training sub-graph
    global_step = tf.train.get_global_step()
    optimizer = tf.train.GradientDescentOptimizer(0.01)
    """Clouds: what is tf.group???"""
    train = tf.group(optimizer.minimize(loss),
                   tf.assign_add(global_step, 1))
    print("--------\n\t_model_fn:train group=", train )
    print("--------\n\n")
    
    # EstimatorSpec connects subgraphs we built to the
    # appropriate functionality.
    return tf.estimator.EstimatorSpec(
          mode=mode,
          predictions=y,
          loss=loss,
          train_op=train)
    
    
    
    
    
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
#     linear_regression()
    linear_regression_tf_estimator()
    
    print("Done!")
    pass