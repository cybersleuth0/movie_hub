import 'package:flutter/material.dart';
import 'package:movieshub/ui_pages/homepage.dart';
import 'package:movieshub/ui_pages/splashScreen_page.dart';

void main() {
  runApp(MoviesApp());
}

class MoviesApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: SplashScreen(),
      debugShowCheckedModeBanner: false,
    );
  }
}
