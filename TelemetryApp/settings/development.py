"""Load using development settings"""
from opentelemetry import trace

# from opentelemetry.instrumentation.django import DjangoInstrumentor
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.trace import Tracer

from .utils import UUIDGenerator

# Create a Resource with a specified service name
resource: Resource = Resource.create({"service.name": "django-telemetry"})

# Set up a tracing provider with a specified Resource
trace_provider: TracerProvider = TracerProvider(
    resource=resource
)
trace.set_tracer_provider(trace_provider)

# Export trace spans to console in batches (for development!)
trace_provider.add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()))

from TelemetryApp.settings.settings import *
