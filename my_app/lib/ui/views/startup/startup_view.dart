import 'package:flutter/material.dart';
import 'package:stacked/stacked.dart' show ViewModelBuilder;

import 'startup_viewmodel.dart';

class StartupView extends StatelessWidget {
  const StartupView({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return ViewModelBuilder<StartupViewModel>.reactive(
      builder: (context, model, child) => Scaffold(),
      viewModelBuilder: () => StartupViewModel(),
    );
  }
}