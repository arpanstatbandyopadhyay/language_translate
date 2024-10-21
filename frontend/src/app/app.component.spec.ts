import { ComponentFixture, TestBed } from '@angular/core/testing';
import { AppComponent } from './app.component';
import { TranslationService } from './translation.service';
import { of, throwError } from 'rxjs';

describe('AppComponent', () => {
  let component: AppComponent;
  let fixture: ComponentFixture<AppComponent>;
  let translationService: jasmine.SpyObj<TranslationService>;

  beforeEach(() => {
    // Create a spy for the TranslationService
    translationService = jasmine.createSpyObj('TranslationService', ['translate']);

    TestBed.configureTestingModule({
      declarations: [AppComponent],
      providers: [
        { provide: TranslationService, useValue: translationService }
      ]
    });

    fixture = TestBed.createComponent(AppComponent);
    component = fixture.componentInstance;
  });

  it('should create the app component', () => {
    expect(component).toBeTruthy();
  });

  it('should translate text successfully', () => {
    const mockResponse = { translation: 'Hello' };
    translationService.translate.and.returnValue(of(mockResponse));

    component.text = 'Hallo';
    component.srcLang = 'de';
    component.tgtLang = 'en';
    component.translate();

    expect(translationService.translate).toHaveBeenCalledWith('Hallo', 'de', 'en');
    expect(component.translation).toBe('Hello');
  });

  it('should handle translation error', () => {
    translationService.translate.and.returnValue(throwError('Translation error'));

    component.text = 'Hallo';
    component.srcLang = 'de';
    component.tgtLang = 'en';
    component.translate();

    expect(translationService.translate).toHaveBeenCalledWith('Hallo', 'de', 'en');
    expect(component.translation).toBe(''); // Expecting no translation on error
    // Optionally, you can also check the console output if needed
  });
});
