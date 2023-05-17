package fr.christophetd.log4shell.vulnerableapp;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.view.RedirectView;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import org.springframework.web.bind.annotation.RestController;

@RestController
public class MainController {
	private static final Logger logger = LogManager.getLogger(MainController.class);

	@GetMapping("/")
	public RedirectView home() {
	    return new RedirectView("/hello?test=World");
	}
	
	@GetMapping("/hello")
	public String hello(@RequestParam(value="test", defaultValue="World") String test) {
	    logger.info("test parameter value: " + test);
	    return "Hello, " + test;
	}
}

