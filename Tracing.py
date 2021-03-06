from enum import Enum
from typing import Any, List

from base import ChromeCommand


class MemoryDumpConfig: pass

class TraceConfig:
    def __init__(self, recordMode: str=None, enableSampling: bool=None, enableSystrace: bool=None, enableArgumentFilter: bool=None, includedCategories: List=None, excludedCategories: List=None, syntheticDelays: List=None, memoryDumpConfig: "MemoryDumpConfig"=None):
        # Controls how the trace buffer stores data.
        self.recordMode = recordMode
        # Turns on JavaScript stack sampling.
        self.enableSampling = enableSampling
        # Turns on system tracing.
        self.enableSystrace = enableSystrace
        # Turns on argument filter.
        self.enableArgumentFilter = enableArgumentFilter
        # Included category filters.
        self.includedCategories = includedCategories
        # Excluded category filters.
        self.excludedCategories = excludedCategories
        # Configuration to synthesize the delays in tracing.
        self.syntheticDelays = syntheticDelays
        # Configuration for memory dump triggers. Used only when "memory-infra" category is enabled.
        self.memoryDumpConfig = memoryDumpConfig

class start(ChromeCommand):
    """Start trace events collection."""

    def __init__(self, categories: str=None, options: str=None, bufferUsageReportingInterval: float=None, transferMode: str=None, traceConfig: "TraceConfig"=None):
        # Category/tag filter
        self.categories = categories
        # Tracing options
        self.options = options
        # If set, the agent will issue bufferUsage events at this interval, specified in milliseconds
        self.bufferUsageReportingInterval = bufferUsageReportingInterval
        # Whether to report trace events as series of dataCollected events or to save trace to a stream (defaults to <code>ReportEvents</code>).
        self.transferMode = transferMode
        # 
        self.traceConfig = traceConfig



class end(ChromeCommand):
    """Stop trace events collection."""

    def __init__(self): pass

class getCategories(ChromeCommand):
    """Gets supported tracing categories."""

    def __init__(self): pass

class requestMemoryDump(ChromeCommand):
    """Request a global memory dump."""

    def __init__(self): pass

class recordClockSyncMarker(ChromeCommand):
    """Record a clock sync marker in the trace."""

    def __init__(self, syncId: str):
        # The ID of this clock sync marker
        self.syncId = syncId



