Place your real photos here with the following filenames so About.html displays them:

- on-the-road.jpg — a photo of Knowledge driving or on the road
- in-the-field.jpg — a photo of Knowledge in the field or with wildlife
- guide-at-site.jpg — a photo of Knowledge at a viewpoint or lodge
- ruins.jpg — a photo of Great Zimbabwe or similar historic ruins

Use high-resolution images. Recommended dimensions: 1600×900 (landscape). Filenames are case-sensitive on some servers; keep them lowercase.

Additional gallery images (place these filenames for the Gallery page):

- gallery-victoria-falls.jpg
- gallery-hwange-dusk.jpg
- gallery-great-zimbabwe.jpg
- gallery-nyanga-sunrise.jpg
- gallery-chimanimani.jpg
- gallery-harare-jacaranda.jpg
- gallery-eastern-highlands.jpg
- gallery-zambezi-sunset.jpg
- gallery-hwange-plains.jpg

Note: I generated lightweight placeholder SVG images with these names but using the .svg extension. You can replace them with real photos by adding files with the same base name and updating the extension to .jpg or .png in the HTML if you prefer real images.

Generated placeholder files added to `assets/images`:

- on-the-road.svg
- in-the-field.svg
- guide-at-site.svg
- ruins.svg
- gallery-victoria-falls.svg
- gallery-hwange-dusk.svg
- gallery-great-zimbabwe.svg
- gallery-nyanga-sunrise.svg
- gallery-chimanimani.svg
- gallery-harare-jacaranda.svg
- gallery-eastern-highlands.svg
- gallery-zambezi-sunset.svg
- gallery-hwange-plains.svg

PowerShell quick-download (runs in the `index` folder):

```powershell
$images = @{
	'on-the-road.jpg' = 'https://source.unsplash.com/1600x900/?road,vehicle,zimbabwe'
	'in-the-field.jpg' = 'https://source.unsplash.com/1600x900/?guide,wildlife,zimbabwe'
	'guide-at-site.jpg' = 'https://source.unsplash.com/1600x900/?guide,viewpoint'
	'ruins.jpg' = 'https://source.unsplash.com/1600x900/?great%20zimbabwe,ruins'
	'gallery-victoria-falls.jpg' = 'https://source.unsplash.com/1600x900/?victoria%20falls,zimbabwe'
	'gallery-hwange-dusk.jpg' = 'https://source.unsplash.com/1600x900/?elephants,waterhole,dusk'
	'gallery-great-zimbabwe.jpg' = 'https://source.unsplash.com/1600x900/?great%20zimbabwe,ruins'
	'gallery-nyanga-sunrise.jpg' = 'https://source.unsplash.com/1600x900/?mountain,sunrise,nyanga'
	'gallery-chimanimani.jpg' = 'https://source.unsplash.com/1600x900/?mountains,chimanimani'
	'gallery-harare-jacaranda.jpg' = 'https://source.unsplash.com/1600x900/?jacaranda,harare'
	'gallery-eastern-highlands.jpg' = 'https://source.unsplash.com/1600x900/?tea,highlands,nyanga'
	'gallery-zambezi-sunset.jpg' = 'https://source.unsplash.com/1600x900/?zambezi,sunset'
	'gallery-hwange-plains.jpg' = 'https://source.unsplash.com/1600x900/?savanna,grassland,hwange'
}

New-Item -ItemType Directory -Force -Path assets\images
Set-Location -Path assets\images
foreach ($name in $images.Keys) {
	Write-Host "Downloading $name..."
	Invoke-WebRequest -Uri $images[$name] -OutFile $name -UseBasicParsing
}
``` 

Notes:
- `source.unsplash.com` serves royalty-free photos for non-commercial use; review licensing if you plan commercial use.
- If you prefer PNGs, change the extension in the keys above and in the HTML.
