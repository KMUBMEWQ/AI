import tensorflow as tf

x1 = tf.constant([1., 2., 3.], dtype=tf.float64)
print(x1)

x2 = tf.cast(x1, tf.int32)
print(x2)

print(tf.reduce_min(x2), tf.reduce_max(x2))