import { Component } from '@angular/core';
import { TranslationService } from './translation.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  text: string = '';
  srcLang: string = 'de';
  tgtLang: string = 'en';
  translation: string = '';

  constructor(private translationService: TranslationService) {}

  translate() {
    this.translationService.translate(this.text, this.srcLang, this.tgtLang).subscribe(
      response => {
        console.log('Translation response:', response);  // Log the response
        this.translation = response.translation;
      },
      error => console.error('Error translating text', error)
    );
  }
  
}
