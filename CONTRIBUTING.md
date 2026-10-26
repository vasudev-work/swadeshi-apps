# Contributing

Thanks for helping. This list is only useful if it stays accurate.

## The one thing that matters most: the package id

A package id looks like `com.zoho.mail`. It is the part after `id=` in a Play link:

```
https://play.google.com/store/apps/details?id=com.zoho.mail
                                             ^^^^^^^^^^^^ this
```

If you send only an app name, the link stays a search link and the icon and category
cannot be filled in. **A package id fixes all three at once.**

## Adding an app

1. Open `data/apps.csv`.
2. Add one row at the end:

```
name,package,developer,category,play_category,play_url,website_url,open_source,status,has_icon
```

3. Add the same row to the matching file in `data/by-category/`.
4. Run the checker:

```bash
python3 scripts/validate.py
```

5. Open a pull request.

You can also just open an issue with a Play link. That is fine too.

## Rules

- **One row per package id.** If two rows share a package, the checker fails on purpose.
- **No invented data.** No ratings, no download counts, no review numbers. If you do not
  know a value, write `Unknown`.
- **Do not rename the categories.** They are used by the app that reads this list.
- **Indian developers only.** The point of the list is apps built in India.
- **Link to the official listing.** Not a mirror, not an APK site.

## Categories in use

`Office, Productivity & AI Utilities` - `Other Indian Apps` -
`Social Media, Messaging & Networking` - `EdTech & Learning` - `Zoho Apps` -
`Media, Streaming & Audio` - `Government, e-Governance & Citizen Services` -
`Fintech, Payments & Banking` - `Health, Fitness & Pharmacy` -
`E-Commerce, Quick-Commerce & Retail` - `Travel, Mobility & Commute` -
`Gaming & Esports` - `Food Delivery, Restaurants & Logistics` -
`Play Store alternatives (not Indian)` - `Indian Native App Store Platforms`
