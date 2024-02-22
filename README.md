# Wiki Encyclopedia Project

The Wiki Encyclopedia project is part of a web development initiative aimed at creating a comprehensive platform for managing encyclopedia entries. This project was undertaken as part of CS50’s Web Programming with Python and JavaScript to showcase skills in web development and user interface design. Below is a summary of the features and requirements implemented in this project:

## Project Summary

The project involves the creation of a user-friendly Wiki Encyclopedia, allowing users to create, view, edit, and search for encyclopedia entries. It provides a seamless experience for users to navigate and contribute to the growing repository of knowledge.

## Requirements

1. **Entry Page:** Users can visit specific entry pages (e.g., `/wiki/TITLE`) to view the contents of individual encyclopedia entries. The title of the page reflects the name of the entry.

2. **Index Page:** The index page (`index.html`) has been enhanced to make each entry name clickable. Users can now navigate directly to the entry page by clicking on the entry name.

3. **Search:** A robust search functionality enables users to type queries into the search box. If a query matches an entry, the user is redirected to that entry's page. Otherwise, a search results page displays entries with the query as a substring.

4. **New Page:** Clicking "Create New Page" allows users to create a new encyclopedia entry. Users can input a title and Markdown content, save the page, and the new entry is added to the collection.

5. **Edit Page:** Each entry page includes a link to edit the entry's Markdown content. Users can make changes, save them, and be redirected back to the entry's page.

6. **Random Page:** Clicking "Random Page" in the sidebar provides users with a serendipitous journey to a randomly selected encyclopedia entry.

7. **Markdown to HTML Conversion:** The `python-markdown2` package is employed to convert Markdown content to HTML, ensuring a readable and polished presentation on each entry's page.

## Project Demo

Watch a demonstration of the Wiki Encyclopedia project on [YouTube](https://youtu.be/6HqeRpGUl88).

Feel free to explore and engage with the Wiki Encyclopedia. If you have any questions or feedback, please don't hesitate to reach out. Happy exploring!
