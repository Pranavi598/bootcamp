from abstraction_level_4.processors.counter import LineCounter
from abstraction_level_4.processors.fan_in import join_two_lines  # This is a function
from abstraction_level_4.processors.fan_out import split_lines  # This is a function


def load_pipeline(config):
    """Load and return the processors as specified in the configuration."""
    processors = []

    for processor_config in config['processors']:
        print(f"Loading processor: {processor_config['type']}")  # Debugging print
        processor_type = processor_config['type']
        options = processor_config.get('options', {})

        # Handle processors
        if processor_type == 'abstraction_level_4.processors.counter.LineCounter':
            processor = LineCounter(**options)
        elif processor_type == 'abstraction_level_4.processors.fan_in.JoinLines':
            # wrap the function `join_two_lines` as a processor
            processor = _wrap_stream_processor(join_two_lines, **options)  # Wrapping function into stream processor
        elif processor_type == 'abstraction_level_4.processors.fan_out.SplitLines':
            # wrap the function `split_lines` as a processor
            processor = _wrap_stream_processor(split_lines, **options)  # Wrapping function into stream processor
        processors.append(processor)

    return processors


def _wrap_stream_processor(processor_function, **options):
    """Wraps a function (like join_two_lines or split_lines) into a processor class."""
    class StreamProcessor:
        def __init__(self, function, **options):
            self.function = function
            self.options = options

        def process(self, input_lines):
            """Process input lines as a stream (Iterator[str] -> Iterator[str])."""
            return self.function(input_lines, **self.options)

    return StreamProcessor(processor_function, **options)
