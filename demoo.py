from flask import Flask
from jaeger_client import Config
from opentracing.propagation import Format

app = Flask(__name__)

# Configure the Jaeger client
config = Config(
    config={
        'sampler': {
            'type': 'const',
            'param': 1,
        },
        'logging': True,
        'local_agent': {
            'reporting_host': '20.237.35.236',
            'reporting_port': 16686,
        },
    },
    service_name='my-flask-app',
    validate=True,
)
tracer = config.initialize_tracer()

# Define a route to generate some trace data
@app.route('/hello')
def hello():
    with tracer.start_active_span('hello') as scope:
        scope.span.log_kv({'event': 'hello'})
        return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)

