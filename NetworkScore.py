
import tensorflow as tf
from layers import GraphConvolution

class Model(object):
    def __init__(self, **kwargs):
        allowed_kwargs = {'name', 'logging'}
        for kwarg in kwargs.keys():
            assert kwarg in allowed_kwargs, 'Invalid keyword argument: ' + kwarg

        for kwarg in kwargs.keys():
            assert kwarg in allowed_kwargs, 'Invalid keyword argument: ' + kwarg
        name = kwargs.get('name')
        if not name:
            name = self.__class__.__name__.lower()
        self.name = name

        logging = kwargs.get('logging', False)
        self.logging = logging

        self.vars = {}

    def _build(self):
        raise NotImplementedError

    def build(self):
        """ Wrapper for _build() """
        with tf.variable_scope(self.name):
            self._build()
        variables = tf.get_collection(tf.GraphKeys.GLOBAL_VARIABLES, scope=self.name)
        self.vars = {var.name: var for var in variables}

    def fit(self):
        pass

    def predict(self):
        pass

"""

    1. Features (the feature of node)
    2. Network (the structure of network)

"""

class NetworkScore(Model):

    def __init__(self, placeholders, num_features, **kwargs):
        super(NetworkScore, self).__init__(**kwargs)
        self.features = placeholders['features']
        self.input_dim1 = placeholders['input_dim1']
        self.output_dim1 = placeholders['output_dim1']

        self.adj = placeholders['adj']
        self.dropout = placeholders['dropout']

    def _build(self):

        self.hidden1 = GraphConvolution(input_dim=self.input_dim,
                                        output_dim=FLAGS.hidden1,
                                        adj=self.adj,
                                        act=tf.nn.relu,
                                        dropout=self.dropout,
                                        logging=self.logging)(self.features)
















