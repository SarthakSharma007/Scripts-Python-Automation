<h1>File Organizer Script</h1>

<p>
This project is a Python-based file organizer that automatically sorts files in a specified directory into categorized subfolders based on their file extensions. It helps maintain a clean and structured workspace by grouping files such as images, documents, data sheets, presentations, archives, applications, code scripts, and media files.
</p>

<h2>Features</h2>
<ul>
    <li>Automatically categorizes files by extension</li>
    <li>Creates required folders if they do not exist</li>
    <li>Moves files safely into their category folders</li>
    <li>Handles duplicate filenames by adding timestamps</li>
    <li>Supports a wide range of file formats</li>
</ul>

<h2>Technologies Used</h2>
<ul>
    <li>Python 3</li>
    <li>os module</li>
    <li>shutil module</li>
    <li>datetime module</li>
</ul>

<h2>File Categories</h2>
<p>The organizer classifies files into the following categories:</p>
<ul>
    <li>Images</li>
    <li>Documents</li>
    <li>Data and Sheets</li>
    <li>Presentations</li>
    <li>Archives</li>
    <li>Applications</li>
    <li>Code Scripts</li>
    <li>Video and Audio Media</li>
    <li>Other Files (default category)</li>
</ul>

<h2>How It Works</h2>
<ol>
    <li>Set the target directory path in the <code>DIRECTORY_TO_ORGANIZE</code> variable.</li>
    <li>The script scans all files in the directory.</li>
    <li>Each file is matched with its corresponding category based on extension.</li>
    <li>If a category folder does not exist, the script creates it.</li>
    <li>Files are moved to their respective folders.</li>
    <li>If a filename already exists, a timestamp is added to avoid overwriting.</li>
</ol>

<h2>Usage</h2>
<pre>
1. Open the script.
2. Replace the value of DIRECTORY_TO_ORGANIZE with your folder path:
   DIRECTORY_TO_ORGANIZE = r"C:\Users\YourName\Downloads"

3. Run the script:
   python organize.py
</pre>

<h2>Code Structure</h2>
<ul>
    <li><strong>get_destination_folder()</strong>: Determines the category of a file.</li>
    <li><strong>organize_files()</strong>: Performs the main organizing logic.</li>
    <li><strong>FILE_TYPE</strong>: Dictionary mapping file extensions to folder names.</li>
    <li><strong>__main__ block</strong>: Entry point of the program.</li>
</ul>

<h2>Error Handling</h2>
<ul>
    <li>Handles missing directory paths</li>
    <li>Manages folder creation errors</li>
    <li>Prevents overwriting files by renaming duplicates</li>
</ul>

<h2>Output</h2>
<p>The script prints logs for:</p>
<ul>
    <li>Files moved successfully</li>
    <li>Duplicate renamed files</li>
    <li>Errors encountered during folder creation or file movement</li>
</ul>

<h2>License</h2>
<p>
This project is free to use and modify for personal or educational purposes.
</p>
