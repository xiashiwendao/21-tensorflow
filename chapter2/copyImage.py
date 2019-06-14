import tensorflow as tf
import os
if not os.path.exists("read"):
    os.mkdir("read")

with tf.Session() as sess:
    file_names = ["A.jpg", "B.jpg", "C.jpg"]
    epochs = 5
    file_queue = tf.train.string_input_producer(file_names, shuffle=False, num_epochs= epochs)
    print("++++++ file queue的值是 ++++++: ", file_queue)
    tf.local_variables_initializer().run() # for num_epochs variable need to be initialized
    threads = tf.train.start_queue_runners(sess=sess)
    reader = tf.WholeFileReader()
    key, value = reader.read(file_queue)
    
    i = 0
    totalCount = epochs * len(file_names)
    for i in range(totalCount):
        image_data = sess.run(value)
        with open("read/image_%d.jpg" % (i+1), "wb") as f:
            f.write(image_data)
