# This file was auto-generated by Fern from our API Definition.

import typing

from .tasks_embed_step import TasksEmbedStep
from .tasks_error_workflow_step import TasksErrorWorkflowStep
from .tasks_get_step import TasksGetStep
from .tasks_log_step import TasksLogStep
from .tasks_prompt_step import TasksPromptStep
from .tasks_return_step import TasksReturnStep
from .tasks_search_step import TasksSearchStep
from .tasks_set_step import TasksSetStep
from .tasks_sleep_step import TasksSleepStep
from .tasks_tool_call_step import TasksToolCallStep
from .tasks_wait_for_input_step import TasksWaitForInputStep
from .tasks_yield_step import TasksYieldStep

TasksCaseThenThen = typing.Union[
    typing.Any,
    TasksToolCallStep,
    TasksYieldStep,
    TasksPromptStep,
    TasksErrorWorkflowStep,
    TasksSleepStep,
    TasksReturnStep,
    TasksGetStep,
    TasksSetStep,
    TasksLogStep,
    TasksEmbedStep,
    TasksSearchStep,
    TasksWaitForInputStep,
]
