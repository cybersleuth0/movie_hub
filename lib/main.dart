import 'package:flutter/material.dart';
import 'package:movieshub/ui_pages/homepage.dart';
import 'package:movieshub/ui_pages/movieDetails_page.dart';
import 'package:movieshub/ui_pages/showmovies_Page.dart';

void main() {
  runApp(MoviesApp());
}

class MoviesApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: HomePage(),
      debugShowCheckedModeBanner: false,
    );
  }
}
