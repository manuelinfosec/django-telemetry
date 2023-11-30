import uuid

from opentelemetry.sdk.trace.id_generator import IdGenerator


class UUIDGenerator(IdGenerator):
    """
    ID Generator for TraceProvider replacing the default random bits
    with UUIDv4.
    """

    def generate_span_id(self) -> uuid.UUID:
        return uuid.uuid4()

    def generate_trace_id(self) -> uuid.UUID:
        return uuid.uuid4()
