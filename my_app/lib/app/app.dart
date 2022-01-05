import 'package:my_app/ui/views/second/second_view.dart';
import 'package:my_app/ui/views/startup/startup_view.dart';
import 'package:stacked/stacked_annotations.dart' show CupertinoRoute, LazySingleton, MaterialRoute, StackedApp;
import 'package:stacked_services/stacked_services.dart';

@StackedApp(
  routes: [
    MaterialRoute(page: StartupView, initial: true),
    CupertinoRoute(page: SecondView)
  ],
  dependencies: [
    LazySingleton(classType: NavigationService),
  ],
)
class AppSetup{}