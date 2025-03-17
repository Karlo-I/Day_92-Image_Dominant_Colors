Below is a self-reflection I have submitted to the course provider after completing the project, which I believe will help provide background for this repository.

Reflection:

After reading through the instructions and examples provided, I began writing down the structure/flow that I thought I needed for the website:

* Homepage setup
* Upload image functionality
* Image processing
* Color extraction from an image
    * Skimmed through tutorials, including Day 76, to see if there was any methodology to identify the RGB values of a given image.
    * Searched for API providers offering free access that don't require bank details:
        * ColorExtraction (RapidAPI)
        * Colormind API
    * Reviewed each API, but none of them worked.
    * Found a comment on StackOverflow suggesting the colorgram module.

After deciding to use colorgram, I tested the suggested code and added a function to convert the RGB values from colorgram into HEX codes.

To resolve some of the bugs encountered and figure out how to add image upload functionality and display the image, I interacted with ChatGPT to find potential solutions.

I also consulted a friend, an experienced programmer, about some of the CSS issues.

When all the functionalities worked for the first time, I then asked ChatGPT to explain each line of code to ensure that I understood everything.

After reviewing ChatGPT’s explanations, I made further changes to the code:

* The .dominant-colors class, which previously held a grid-template-columns parameter with a value of 4, was updated to 5 equal columns.
* The text "Copy" inside the buttons was centered by updating the CSS for .color-item and .color-item-button.
* Changed the shape of the copy buttons.
* Added an H5 tag with the text "HEX Code (Percentage)."

Finally, I then cleaned up the file (a similar exercise I did in Day 91 with my friend) by separating some of the functions into separate Python files.
