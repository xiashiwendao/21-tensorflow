import tensorflow as tf
import numpy as np


two_node = tf.constant(2)
print(two_node)
three_node = tf.constant(3)
print(three_node)
sum_node = two_node + three_node
with tf.Session() as sess:
    value = sess.run([two_node, sum_node])
    print(value)

place_holder = tf.placeholder(tf.int32)
with tf.Session() as sess:
    result = sess.run(place_holder, feed_dict={place_holder:5})
    print("result is: ", result)

# 初始化的节点一定要赋值（assign）才可以被session run
tf.reset_default_graph()
var_value = tf.get_variable("count", [], tf.int32)
zero = tf.constant(0)
assign_node = tf.assign(var_value, zero)
with tf.Session() as sess:
    result = sess.run(assign_node)
    print("variable value: ", result)

tf.reset_default_graph()
const_init = tf.constant_initializer(0.)
count_var = tf.get_variable("count", [], initializer=const_init)
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    print("init count value: ", sess.run(count_var))

import time
import pandas as pd
data_path = "C:\\Users\\wenyang.zhang\\Documents\\MySpace\\Workspace\\SalesAnalies\\data\\"
file_name = "data(3).xlsx"
start = time.time()
data = pd.read_excel(data_path + file_name, sheet_name="Value", header=5, usecols="C:AO")
data.head()
end = time.time()
print("cost time: ", (end - start))