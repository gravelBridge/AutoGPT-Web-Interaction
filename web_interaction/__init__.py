"""This is the web interaction plugin for Auto-GPT."""
from typing import Any, Dict, List, Optional, Tuple, TypeVar, TypedDict
from auto_gpt_plugin_template import AutoGPTPluginTemplate
from colorama import Fore

PromptGenerator = TypeVar("PromptGenerator")


class Message(TypedDict):
    role: str
    content: str


class AutoGPTWebInteraction(AutoGPTPluginTemplate):
    """
    This is the Auto-GPT web interaction plugin.
    """

    def __init__(self):
        super().__init__()
        self._name = "Auto-Web-Interaction-Plugin"
        self._version = "0.1.0"
        self._description = "Auto-GPT Web Interaction Plugin: Interact with websites."

    def post_prompt(self, prompt: PromptGenerator) -> PromptGenerator:
        from .web_interaction import (
            start_browser,
            go_to_page,
            scroll,
            click,
            type,
            enter,
            crawl,
            type_and_enter,
            get_current_url,
        )

        prompt.add_resource("""
        Ability to interact with websites via the web_interaction plugin. Information for the web_interaction plugin: 
        The format of the browser content is highly simplified; all formatting elements are stripped.
        Interactive elements such as links, inputs, buttons are represented like this:

		    <link id=1>text</link>
		    <button id=2>text</button>
		    <input id=3>text</input>

        Images are rendered as their alt text like this:

		    <img id=4 alt=""/>

        Don't try to interact with elements that you can't see.

        CRITICAL: The id parameter specified in <img id=4 alt=""/>, <link id=1>text</link>, <button id=2>text</button> etc.. MUST be used for all web_interaction commands that require an id.
        CRITICAL: Use the command get_dom every time before executing any web_interaction plugin command.
        CRITICAL: When trying to search something on Google, don't call the dom function. Instead, just use the id value of 3
        """)

        prompt.add_command("start_browser", "Starts the browser for web interaction. Must be ran before attempting to perform any other web interaction plugins.", {}, start_browser)

        prompt.add_command("go_to_website", "Goes to a website in the web interaction plugin. Must be ran after starting the browser and before attempting to interact with a website.", {"url":"<url>"}, go_to_page)

        prompt.add_command("get_dom", "Returns a simplified DOM of the current web page. The id is specific to this plugin and will be needed to interact with elements. Make sure to run this before interacting with any elements on a webpage. Re-run this each time you're on a new webpage and want to interact with elements.", {}, crawl)

        prompt.add_command("click_element_by_id", "Clicks an element. Specify the id with the unique id received from the get_dom command. CRITICAL: The ID must be the integer id from the get_dom command.", {"id":"<id>"}, click)

        prompt.add_command("input_text_by_id", "Inputs text to an element. Specify the id with the unique id received from the get_dom command. CRITICAL: The ID must be the integer id from the get_dom command.", {"id":"<id>", "text":"<text>"}, type)

        prompt.add_command("input_text_by_id_and_press_enter", "Inputs text to an element. Specify the id with the unique id received from the get_dom command. Also presses enter after finishing inputting text. CRITICAL: The ID must be the integer id from the get_dom command.", {"id":"<id>", "text":"<text>"}, type_and_enter)

        prompt.add_command("scroll", "Scrolls the current website up or down one page. In the arguments, use either \"up\" or \"down\"", {"direction":"<directionToScroll>"}, scroll)

        prompt.add_command("enter", "Presses enter on the keyboard on the current website.", {}, enter)

        prompt.add_command("get_url", "Retrieves the current url that the web_interaction plugin is on.", {}, get_current_url)

        return prompt


    def can_handle_post_prompt(self) -> bool:
        """This method is called to check that the plugin can
        handle the post_prompt method.

        Returns:
            bool: True if the plugin can handle the post_prompt method."""
        return True

    def can_handle_on_response(self) -> bool:
        """This method is called to check that the plugin can
        handle the on_response method.

        Returns:
            bool: True if the plugin can handle the on_response method."""
        return False

    def on_response(self, response: str, *args, **kwargs) -> str:
        """This method is called when a response is received from the model."""
        pass

    def can_handle_on_planning(self) -> bool:
        """This method is called to check that the plugin can
        handle the on_planning method.

        Returns:
            bool: True if the plugin can handle the on_planning method."""
        return False

    def on_planning(
        self, prompt: PromptGenerator, messages: List[Message]
    ) -> Optional[str]:
        """This method is called before the planning chat completion is done.

        Args:
            prompt (PromptGenerator): The prompt generator.
            messages (List[str]): The list of messages.
        """
        pass

    def can_handle_post_planning(self) -> bool:
        """This method is called to check that the plugin can
        handle the post_planning method.

        Returns:
            bool: True if the plugin can handle the post_planning method."""
        return False

    def post_planning(self, response: str) -> str:
        """This method is called after the planning chat completion is done.

        Args:
            response (str): The response.

        Returns:
            str: The resulting response.
        """
        pass

    def can_handle_pre_instruction(self) -> bool:
        """This method is called to check that the plugin can
        handle the pre_instruction method.

        Returns:
            bool: True if the plugin can handle the pre_instruction method."""
        return False

    def pre_instruction(self, messages: List[Message]) -> List[Message]:
        """This method is called before the instruction chat is done.

        Args:
            messages (List[Message]): The list of context messages.

        Returns:
            List[Message]: The resulting list of messages.
        """
        pass

    def can_handle_on_instruction(self) -> bool:
        """This method is called to check that the plugin can
        handle the on_instruction method.

        Returns:
            bool: True if the plugin can handle the on_instruction method."""
        return False

    def on_instruction(self, messages: List[Message]) -> Optional[str]:
        """This method is called when the instruction chat is done.

        Args:
            messages (List[Message]): The list of context messages.

        Returns:
            Optional[str]: The resulting message.
        """
        pass

    def can_handle_post_instruction(self) -> bool:
        """This method is called to check that the plugin can
        handle the post_instruction method.

        Returns:
            bool: True if the plugin can handle the post_instruction method."""
        return False

    def post_instruction(self, response: str) -> str:
        """This method is called after the instruction chat is done.

        Args:
            response (str): The response.

        Returns:
            str: The resulting response.
        """
        pass

    def can_handle_pre_command(self) -> bool:
        """This method is called to check that the plugin can
        handle the pre_command method.

        Returns:
            bool: True if the plugin can handle the pre_command method."""
        return False

    def pre_command(
        self, command_name: str, arguments: Dict[str, Any]
    ) -> Tuple[str, Dict[str, Any]]:
        """This method is called before the command is executed.

        Args:
            command_name (str): The command name.
            arguments (Dict[str, Any]): The arguments.

        Returns:
            Tuple[str, Dict[str, Any]]: The command name and the arguments.
        """
        pass

    def can_handle_post_command(self) -> bool:
        """This method is called to check that the plugin can
        handle the post_command method.

        Returns:
            bool: True if the plugin can handle the post_command method."""
        return False

    def post_command(self, command_name: str, response: str) -> str:
        """This method is called after the command is executed.

        Args:
            command_name (str): The command name.
            response (str): The response.

        Returns:
            str: The resulting response.
        """
        pass

    def can_handle_chat_completion(
        self, messages: Dict[Any, Any], model: str, temperature: float, max_tokens: int
    ) -> bool:
        """This method is called to check that the plugin can
          handle the chat_completion method.

        Args:
            messages (List[Message]): The messages.
            model (str): The model name.
            temperature (float): The temperature.
            max_tokens (int): The max tokens.

          Returns:
              bool: True if the plugin can handle the chat_completion method."""
        return False

    def handle_chat_completion(
        self, messages: List[Message], model: str, temperature: float, max_tokens: int
    ) -> str:
        """This method is called when the chat completion is done.

        Args:
            messages (List[Message]): The messages.
            model (str): The model name.
            temperature (float): The temperature.
            max_tokens (int): The max tokens.

        Returns:
            str: The resulting response.
        """
        pass
        
    def can_handle_text_embedding(
        self, text: str
    ) -> bool:
        return False

    def handle_text_embedding(
        self, text: str
    ) -> list:
        pass

    def can_handle_user_input(self, user_input: str) -> bool:
        return False

    def user_input(self, user_input: str) -> str:
        return user_input

    def can_handle_report(self) -> bool:
        return False

    def report(self, message: str) -> None:
        pass

