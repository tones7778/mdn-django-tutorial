https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Tutorial_local_library_website

Common field arguments
The following common arguments can be used when declaring many/most of the different field types:

help_text: Provides a text label for HTML forms (e.g. in the admin site), as described above.
verbose_name: A human-readable name for the field used in field labels. If not specified, Django will infer the default verbose name from the field name.
default: The default value for the field. This can be a value or a callable object, in which case the object will be called every time a new record is created.
null: If True, Django will store blank values as NULL in the database for fields where this is appropriate (a CharField will instead store an empty string). The default is False.
blank: If True, the field is allowed to be blank in your forms. The default is False, which means that Django's form validation will force you to enter a value. This is often used with null=True , because if you're going to allow blank values, you also want the database to be able to represent them appropriately.
choices: A group of choices for this field. If this is provided, the default corresponding form widget will be a select box with these choices instead of the standard text field.
primary_key: If True, sets the current field as the primary key for the model (A primary key is a special database column designated to uniquely identify all the different table records). If no field is specified as the primary key then Django will automatically add a field for this purpose.
There are many other options — you can view the full list of field options here.
https://docs.djangoproject.com/en/2.1/ref/models/fields/#field-options

Common field types
The following list describes some of the more commonly used types of fields. 

CharField is used to define short-to-mid sized fixed-length strings. You must specify the max_length of the data to be stored.
TextField is used for large arbitrary-length strings. You may specify a max_length for the field, but this is used only when the field is displayed in forms (it is not enforced at the database level).
IntegerField is a field for storing integer (whole number) values, and for validating entered values as integers in forms.
DateField and DateTimeField are used for storing/representing dates and date/time information (as Python datetime.date in and datetime.datetime objects, respectively). These fields can additionally declare the (mutually exclusive) parameters auto_now=True (to set the field to the current date every time the model is saved), auto_now_add (to only set the date when the model is first created) , and default (to set a default date that can be overridden by the user).
EmailField is used to store and validate email addresses.
FileField and ImageField are used to upload files and images respectively (the ImageField simply adds additional validation that the uploaded file is an image). These have parameters to define how and where the uploaded files are stored.
AutoField is a special type of IntegerField that automatically increments. A primary key of this type is automatically added to your model if you don’t explicitly specify one.
ForeignKey is used to specify a one-to-many relationship to another database model (e.g. a car has one manufacturer, but a manufacturer can make many cars). The "one" side of the relationship is the model that contains the "key" (models containing a "foreign key" referring to that "key", are on the "many" side of such a relationship).
ManyToManyField is used to specify a many-to-many relationship (e.g. a book can have several genres, and each genre can contain several books). In our library app we will use these very similarly to ForeignKeys, but they can be used in more complicated ways to describe the relationships between groups. These have the parameter on_delete to define what happens when the associated record is deleted (e.g. a value of models.SET_NULL would simply set the value to NULL).
https://docs.djangoproject.com/en/2.1/ref/models/fields/#field-types


https://docs.djangoproject.com/en/2.1/ref/models/options/

https://pypi.org/project/django-extensions/
python manage.py runserver_plus --print-sql

https://github.com/django-admin-bootstrapped/django-admin-bootstrapped
sudo apt-get install python3-dev graphviz libgraphviz-dev pkg-config
pip install pygraphviz
python manage.py graph_models -a -o locallibrary.png# mdn-django-tutorial



The first thing to know is that regular expressions should usually be declared using the raw string literal syntax (i.e. they are enclosed as shown: r'<your regular expression text goes here>').

The main parts of the syntax you will need to know for declaring the pattern matches are:

Symbol	Meaning
^	Match the beginning of the text
$	Match the end of the text
\d	Match a digit (0, 1, 2, ... 9)
\w	Match a word character, e.g. any upper- or lower-case character in the alphabet, digit or the underscore character (_)
+	Match one or more of the preceding character. For example, to match one or more digits you would use \d+. To match one or more "a" characters, you could use a+
*	Match zero or more of the preceding character. For example, to match nothing or a word you could use \w*
( )	Capture the part of the pattern inside the brackets. Any captured values will be passed to the view as unnamed parameters (if multiple patterns are captured, the associated parameters will be supplied in the order that the captures were declared).
(?P<name>...)	Capture the pattern (indicated by ...) as a named variable (in this case "name"). The captured values are passed to the view with the name specified. Your view must therefore declare an argument with the same name!
[  ]	Match against one character in the set. For example, [abc] will match on 'a' or 'b' or 'c'. [-\w] will match on the '-' character or any word character.
Most other characters can be taken literally!

Let's consider a few real examples of patterns:

Pattern	Description
r'^book/(?P<pk>\d+)$'	
This is the RE used in our URL mapper. It matches a string that has book/ at the start of the line (^book/), then has one or more digits (\d+), and then ends (with no non-digit characters before the end of line marker).

It also captures all the digits (?P<pk>\d+) and passes them to the view in a parameter named 'pk'. The captured values are always passed as a string!

For example, this would match book/1234 , and send a variable pk='1234' to the view.

r'^book/(\d+)$'	This matches the same URLs as the preceding case. The captured information would be sent as an unnamed argument to the view.
r'^book/(?P<stub>[-\w]+)$'	
This matches a string that has book/ at the start of the line (^book/), then has one or more characters that are either a '-' or a word character ([-\w]+), and then ends. It also captures this set of characters and passes them to the view in a parameter named 'stub'.

This is a fairly typical pattern for a "stub". Stubs are URL-friendly word-based primary keys for data. You might use a stub if you wanted your book URL to be more informative. For example /catalog/book/the-secret-garden rather than /catalog/book/33.
