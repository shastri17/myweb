### Version 2.2.3 - August 21, 2016

- **Button/Dropdown** - Fixed issue where `ui dropdown button` could have incorrect spacing for dropdown icon **Thanks @ilanus** [#4408](https://github.com/Semantic-Org/Semantic-UI/issues/4408)
- **Icon** - `icons` can now receive `link` styling  **Thanks @tbracken** [#4399](https://github.com/Semantic-Org/Semantic-UI/issues/4399)
- **Dropdown** - `dropdown icon` no longer relies on stopping event propagation. This means using the dropdown icon will now cause other dropdowns to correctly hide. [#3998](https://github.com/Semantic-Org/Semantic-UI/issues/3998)
- **Icon** - Fixed missing `dribbble` icon due to incorrect count of "b" (should be 3). [#4185](https://github.com/Semantic-Org/Semantic-UI/issues/4185)
- **Icon** - Fixes `grab icon` and `television icon` not appearing correctly [#4178](https://github.com/Semantic-Org/Semantic-UI/issues/4178)
- **Icon** - Fixes `talk` icon not working correctly **Thanks @anantogosh** [#4354](https://github.com/Semantic-Org/Semantic-UI/issues/4354)
- **Icons** - Fixed some duplicate icons (External) and mispelled icons (Dribbble)

### Version 2.2.0 - June 26, 2016

- **Icons** -  Icons now use the latest Font Awesome `4.6.3` Icons. 80+ new icons+ are included. Thanks @BreadMaker for the PR and @davegandy for the font!
- **Button** - `right icon` like `right arrow icon` would have additional margin inside an `icon button` [#3525](https://github.com/Semantic-Org/Semantic-UI/issues/3525)
- **Icon** - Sizes smaller tham `small` were using with `rem` [#3782](https://github.com/Semantic-Org/Semantic-UI/issues/3782)

### Version 2.1.4 - Sep 13, 2015

- **Button** - Fixes `right labeled icon button` with a `right` named icon (for example `right arrow`) having incorrect margin on icon. [#2973](https://github.com/Semantic-Org/Semantic-UI/issues/2973)

### Version 2.1.3 - Sep 03, 2015

- **Input** - Fixes regression where `ui icon input` inside forms were not correct width [#2953](https://github.com/Semantic-Org/Semantic-UI/issues/2953)

#### Features

- **Icon** - Added `fitted` icon variation, and new small sizes `tiny` and `mini`
- **Menu** - Appearance of `labeled icon menu` has been modified. Horizontal menus now have icons above text, and icons are slightly larger than before.
- **GitHub Theme** - Added github icon theme with port of Octicons.

#### Bugs

- **Icon** - Fixed typo in cube icon alias caused by bad grep [#2765](https://github.com/Semantic-Org/Semantic-UI/issues/2765)
- **Input** - Fixed issue with appearance of `left corner labeled left icon input` [#2782](https://github.com/Semantic-Org/Semantic-UI/issues/2782)
- **Icons** - Fixed issue where `active icon` or `emphasized icon` would not adjust opacity inside menus
- **Menu** - Fix text align on `dropdown item` inside `icon menu`

### Version 2.0.7 - July 23, 2015

- **Dropdown** - Fixed border radius on `circular labeled icon button`  [#2700](https://github.com/Semantic-Org/Semantic-UI/issues/2700)

### Version 2.0.5 - July 20, 2015

- **Message** - Fixed issues where icon would overlap in `icon message` when at mobile resolutions due to `flex-collapse` value being incorrect [#2665](https://github.com/Semantic-Org/Semantic-UI/issues/2665)

### Version 2.0.4 - July 17, 2015

- **Message** - Fixes `attached icon message` not using `flex`

### Version 2.0.3 - July 8, 2015

- **Icon** - `black icon` have been added back as a color option [#2556](https://github.com/Semantic-Org/Semantic-UI/issues/2556)
- **Icon** - Adds missing `square` and `square outline` icon [#2532](https://github.com/Semantic-Org/Semantic-UI/issues/2532)

### Version 2.0.2 - July 7, 2015

- **Dropdown** - Dropdown icon will now always toggle menu visibility [#2510](https://github.com/Semantic-Org/Semantic-UI/issues/2510)

### Version 2.0.0 - June 30, 2015

- **Input** - `pointer-events` have been removed from `icon` in `icon input` unless a `link icon` is used. This is to make sure the hitbox for focusing an input includes the icon.
- **Message** - `icon message` now uses `flexbox` for layout
- **Checkbox** - Reduced kb size of icon font
- **Divider** - Fixes single icon alignment inside `vertical divider` or `horizontal divider`
- **Dropdown** - Fixed `inline dropdown` icon not aligning with content
- **Form** - Fixed autocompleted `ui selection dropdown` having dropdown icon z-index issues
- **Icon** - Fixes `ascending` and `descending` icon being swapped
- **Icon** - Fixes phone icon only appearing as alias `call`
- **Input** - Fixed improper left padding on `transparent left icon input` **Thanks @zxfwinder**
- **Message** - Close icon position adjusted to align with headers
- **Search** - Fix `loading search` with an `icon button` causing double loaders.
- **Table** - Fixes `sorted` column are not correctly centered with `center aligned` due to margin on sort icon
- **Table** - Fixes `ascending` and `descending` icons were reversed in table
- **Icon** - `disabled icon` now have `pointer-events` again.

### Version 1.11.0 - March 3, 2015

- **Icon** - added `@src` variable to make it adjustable with themes that dont support all types like `woff2`
- **Icon** - Fix `clockwise rotated icon` causing `clockwise` icon to appear

### UI Changes

- **Icon** - Added Font Awesome 4.3 including many new icons
- **Dropdown** - `search selection dropdown` will now close the menu when a `dropdown icon` is clicked
- **Icon** - Added woff2 icon files for supported browsers (20% file-size decrease) **Thanks FontAwesome**
- **Breadcrumb** - Breadcrumb icon now has exact px value to alleviate vertical align issues
- **Dropdown** - Upward dropdown now has upward arrow icon
- **Icon** - `external link` and `external link square` has been renamed to `external icon` to no longer receive `link` styles by default
- **Modal** - Modal now swaps to `scrolling modal` when `close icon` no longer can be displayed, instead of modal `content`

### Version 1.7.0 - January 14, 2015

- **Dropdown** - Fixed bug where sub menus may sometimes have dropdown icon overlap text
- **Button** - Fix issue with labeled icon groups in material theme

### Version 1.6.4 - January 12, 2015

- **Build** - Fix CSS property typo in list icon, and label causing issues with some custom build tools

### Version 1.6.3 - January 12, 2015

- **Build** - Fix CSS property typo in list icon, and label causing issues with some custom build tools

### Version 1.6.0 - January 05, 2015

- **Menu** - Fixes ``ui fluid labeled icon menu`` to not have `min-width`

### Version 1.5.0 - December 30, 2014

- **Input** - Fixed bug when ``ui action input`` uses a ``ui icon button``, button was receiving `i.icon` formatting.
- **List** - Fixed bug when using ``ui icon button`` or ``ui icon header`` causing element to receive icon formatting

### Version 1.3.0 - December 17, 2014

- **Dropdown** - Dropdown can now specify which direction a menu should appear left/right, dropdown icons can also appear on the left
- **Step** - Fix issue with completed ordered step icon alignment

### Version 1.1.0 - December 02, 2014

- **Icon** - ``remove icon`` is now formatted correctly when used as ``remove link icon``

### Version 1.0.1 - November 28, 2014

- **Icon** - Fix horizontal centering of circular icon

### Version 1.0.0 - November 24, 2014

- **Form** - Date field has been removed, use a ``ui icon input`` with a ``calendar icon`` instead
- **Label** - Corner labels no longer support text, only icons.
- **Header / Icon** - Inverted headers and icons no longer invert background colors, but instead use a lighter version of colors more legible on dark backgrounds. Inverted circular icons, still however invert the color of the circle.
- **Accordion** - Accordion now includes all icons in an embedded font instead of requiring icons
- **Rating** - Rating now uses an embedded icon font to maximize compatibility
- **Rating** - Rating can now automatically generate icons without including them
- **Steps** - Steps can now have icons, descriptions and titles. Step default theme has been modified significantly to be more flexible.

### Version 0.15.5 - April 11, 2014

- **Message** - Fixes hidden/visible class to set proper display on ``ui icon message``
- **Message** - Fixes hitbox/position of ``close icon`` inside message

### Version 0.15.2 - Mar 28, 2014

- **Icon** - Orange color is now available for icon

### Version 0.15.0 - Mar 14, 2014

- **Icon** - Icons on dark backgrounds should render better in OSX
- **Icon** - Hide and unhide icon were accidentally given opposite names

### Version 0.13.0 - Feb 20, 2014

- **Menu** - Fixes formatting of grouped icon buttons inside menus

### Version 0.12.2 - Jan 21, 2014

- **Icon** - Fixes ascending alphabetic inheritance

### Version 0.12.1 - Jan 15, 2014

- **Message** - Prevents close icon from being misformatted in icon message **thanks MohammadYounes**
- **Icons** - Fixes some icon code samples in docs **thanks mishak87**

### Version 0.12.0 - Jan 06, 2014

- **Icon** - Fixes unnecessary formatting on thumbs up/down

### Version 0.9.6 - Dec 04, 2013

- **Message** - Fixes issues with attached icon message (thanks overra)

### Version 0.9.0 - Nov 5, 2013

- **Button** - Basic icons now have inverted style
- **Input** - Labeled icons now have smaller corner labels
- **Header** - Fixes alignment of solo icons in headers
- **Button** - Fixes labeled icon placement in Chrome

### Version 0.8.3 - Oct 30, 2013

- **Form** - Errored fields now have their icons and corner labels colored appropriately

### Version 0.8.2 - Oct 28, 2013

- **Button** - Fixes button height issue with button groups including icon and normal buttons

### Version 0.7.1 - Oct 23, 2013

- **Dropdown** - Fixes issue with dropdown icon position in chrome

### Version 0.7.0 - Oct 22, 2013

- **List** - Horizontal padding on icon list slightly increased, fixes to icon position
- **Message** - Increase opacity of icons on icon messages

### Version 0.6.1 - Oct 15, 2013

- Adds clockwise/counterclockwise rotated icon and default rotate
- Fixes inheritance issues with rotated icon

### Version 0.3.5 - Oct 2, 2013

- Fixes header content display in icon headers

### Version 0.3.4 - Oct 2, 2013

- Centering of content in icon header

### Version 0.3.3 - Oct 2, 2013

- Headers and lists with icons now do not break with multiline content

### Version 0.3.2 - Oct 2, 2013

- Dropdown now formats top and right arrow icons automatically with icon coupling with sub menus
- List items display issues with icons + content
- Fixes icon input inside a menu placement issues

### Version 0.2.4 - Sep 28, 2013

- Fixes issues with concatenated version receiving conflicted icon definitions causing icons to not function

### Version 0.2.1 - Sep 28, 2013

- Modals can now have an icon in its left content that will be automatically formatted

### Version 0.1.0 - Sep 25, 2013

- Added new font icon set using Font Awesome port
- Adds dropdown icon sexiness to accordions, now with rotating pointing arrows
- Added old icon set as a separate basic icon set
-  Rating icon missing font content with icon font update
- Fixes display of left corner icon labels