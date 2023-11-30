from logging import Logger

from opentelemetry import trace
from opentelemetry.sdk.trace import Span, Tracer
from opentelemetry.trace.status import StatusCode
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class SampleView(APIView):
    """A sample view for testing traces"""

    # Create a span and add to context for use within this view
    @trace.get_tracer(__name__).start_as_current_span("Sample View")
    def get(self, request: Request, *args, **kwargs) -> Response:
        # Default status code for this method
        STATUS_CODE: int = status.HTTP_200_OK

        # Get the current span from context
        span: Span = trace.get_current_span()

        # Initialize a logger for use withing the span
        logger: Logger = trace.getLogger(__name__)

        # Actual method logic
        try:
            logger.info("Reached the view interesting")
            trace.get_current_span().add_event("An event within this trace")

            # trace.Span.add_event(name=request.headers["Accept-Encoding"])
            response: dict = {"message": "Valid response"}

        except Exception as error:
            # Handle exceptions and log correctly
            span.set_status(StatusCode.ERROR, str(error))
            logger.error(f"An error occurred {str(error)}")

            response: dict = {"message": str(error)}
            STATUS_CODE: int = status.HTTP_400_BAD_REQUEST

        return Response(response, status=STATUS_CODE)
