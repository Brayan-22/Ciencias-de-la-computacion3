// Generated from /home/alejandro/Documentos/semestres/novenoSemestre/ciencias3/Ciencias-de-la-computacion3/proyectoCompilador/src/myantlr4/javaAntlr4/MyJava.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class SimpleJavaLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, ID=20, INT=21, WS=22;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"T__9", "T__10", "T__11", "T__12", "T__13", "T__14", "T__15", "T__16", 
			"T__17", "T__18", "ID", "INT", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'class'", "'{'", "'public'", "'static'", "'void'", "'main'", "'('", 
			"'String'", "'['", "']'", "')'", "'}'", "'int'", "'='", "';'", "'if'", 
			"'else'", "'while'", "'+'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, "ID", "INT", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public SimpleJavaLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "MyJava.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u0016\u0087\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0002\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014"+
		"\u0002\u0015\u0007\u0015\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\b\u0001\b\u0001\t\u0001\t\u0001\n\u0001\n\u0001\u000b"+
		"\u0001\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001\u000e"+
		"\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0013"+
		"\u0004\u0013x\b\u0013\u000b\u0013\f\u0013y\u0001\u0014\u0004\u0014}\b"+
		"\u0014\u000b\u0014\f\u0014~\u0001\u0015\u0004\u0015\u0082\b\u0015\u000b"+
		"\u0015\f\u0015\u0083\u0001\u0015\u0001\u0015\u0000\u0000\u0016\u0001\u0001"+
		"\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f"+
		"\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u001b\u000e\u001d\u000f"+
		"\u001f\u0010!\u0011#\u0012%\u0013\'\u0014)\u0015+\u0016\u0001\u0000\u0003"+
		"\u0002\u0000AZaz\u0001\u000009\u0003\u0000\t\n\r\r  \u0089\u0000\u0001"+
		"\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005"+
		"\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001"+
		"\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000"+
		"\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000"+
		"\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000"+
		"\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0000\u0019\u0001\u0000"+
		"\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000\u0000\u001d\u0001\u0000"+
		"\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000\u0000!\u0001\u0000\u0000"+
		"\u0000\u0000#\u0001\u0000\u0000\u0000\u0000%\u0001\u0000\u0000\u0000\u0000"+
		"\'\u0001\u0000\u0000\u0000\u0000)\u0001\u0000\u0000\u0000\u0000+\u0001"+
		"\u0000\u0000\u0000\u0001-\u0001\u0000\u0000\u0000\u00033\u0001\u0000\u0000"+
		"\u0000\u00055\u0001\u0000\u0000\u0000\u0007<\u0001\u0000\u0000\u0000\t"+
		"C\u0001\u0000\u0000\u0000\u000bH\u0001\u0000\u0000\u0000\rM\u0001\u0000"+
		"\u0000\u0000\u000fO\u0001\u0000\u0000\u0000\u0011V\u0001\u0000\u0000\u0000"+
		"\u0013X\u0001\u0000\u0000\u0000\u0015Z\u0001\u0000\u0000\u0000\u0017\\"+
		"\u0001\u0000\u0000\u0000\u0019^\u0001\u0000\u0000\u0000\u001bb\u0001\u0000"+
		"\u0000\u0000\u001dd\u0001\u0000\u0000\u0000\u001ff\u0001\u0000\u0000\u0000"+
		"!i\u0001\u0000\u0000\u0000#n\u0001\u0000\u0000\u0000%t\u0001\u0000\u0000"+
		"\u0000\'w\u0001\u0000\u0000\u0000)|\u0001\u0000\u0000\u0000+\u0081\u0001"+
		"\u0000\u0000\u0000-.\u0005c\u0000\u0000./\u0005l\u0000\u0000/0\u0005a"+
		"\u0000\u000001\u0005s\u0000\u000012\u0005s\u0000\u00002\u0002\u0001\u0000"+
		"\u0000\u000034\u0005{\u0000\u00004\u0004\u0001\u0000\u0000\u000056\u0005"+
		"p\u0000\u000067\u0005u\u0000\u000078\u0005b\u0000\u000089\u0005l\u0000"+
		"\u00009:\u0005i\u0000\u0000:;\u0005c\u0000\u0000;\u0006\u0001\u0000\u0000"+
		"\u0000<=\u0005s\u0000\u0000=>\u0005t\u0000\u0000>?\u0005a\u0000\u0000"+
		"?@\u0005t\u0000\u0000@A\u0005i\u0000\u0000AB\u0005c\u0000\u0000B\b\u0001"+
		"\u0000\u0000\u0000CD\u0005v\u0000\u0000DE\u0005o\u0000\u0000EF\u0005i"+
		"\u0000\u0000FG\u0005d\u0000\u0000G\n\u0001\u0000\u0000\u0000HI\u0005m"+
		"\u0000\u0000IJ\u0005a\u0000\u0000JK\u0005i\u0000\u0000KL\u0005n\u0000"+
		"\u0000L\f\u0001\u0000\u0000\u0000MN\u0005(\u0000\u0000N\u000e\u0001\u0000"+
		"\u0000\u0000OP\u0005S\u0000\u0000PQ\u0005t\u0000\u0000QR\u0005r\u0000"+
		"\u0000RS\u0005i\u0000\u0000ST\u0005n\u0000\u0000TU\u0005g\u0000\u0000"+
		"U\u0010\u0001\u0000\u0000\u0000VW\u0005[\u0000\u0000W\u0012\u0001\u0000"+
		"\u0000\u0000XY\u0005]\u0000\u0000Y\u0014\u0001\u0000\u0000\u0000Z[\u0005"+
		")\u0000\u0000[\u0016\u0001\u0000\u0000\u0000\\]\u0005}\u0000\u0000]\u0018"+
		"\u0001\u0000\u0000\u0000^_\u0005i\u0000\u0000_`\u0005n\u0000\u0000`a\u0005"+
		"t\u0000\u0000a\u001a\u0001\u0000\u0000\u0000bc\u0005=\u0000\u0000c\u001c"+
		"\u0001\u0000\u0000\u0000de\u0005;\u0000\u0000e\u001e\u0001\u0000\u0000"+
		"\u0000fg\u0005i\u0000\u0000gh\u0005f\u0000\u0000h \u0001\u0000\u0000\u0000"+
		"ij\u0005e\u0000\u0000jk\u0005l\u0000\u0000kl\u0005s\u0000\u0000lm\u0005"+
		"e\u0000\u0000m\"\u0001\u0000\u0000\u0000no\u0005w\u0000\u0000op\u0005"+
		"h\u0000\u0000pq\u0005i\u0000\u0000qr\u0005l\u0000\u0000rs\u0005e\u0000"+
		"\u0000s$\u0001\u0000\u0000\u0000tu\u0005+\u0000\u0000u&\u0001\u0000\u0000"+
		"\u0000vx\u0007\u0000\u0000\u0000wv\u0001\u0000\u0000\u0000xy\u0001\u0000"+
		"\u0000\u0000yw\u0001\u0000\u0000\u0000yz\u0001\u0000\u0000\u0000z(\u0001"+
		"\u0000\u0000\u0000{}\u0007\u0001\u0000\u0000|{\u0001\u0000\u0000\u0000"+
		"}~\u0001\u0000\u0000\u0000~|\u0001\u0000\u0000\u0000~\u007f\u0001\u0000"+
		"\u0000\u0000\u007f*\u0001\u0000\u0000\u0000\u0080\u0082\u0007\u0002\u0000"+
		"\u0000\u0081\u0080\u0001\u0000\u0000\u0000\u0082\u0083\u0001\u0000\u0000"+
		"\u0000\u0083\u0081\u0001\u0000\u0000\u0000\u0083\u0084\u0001\u0000\u0000"+
		"\u0000\u0084\u0085\u0001\u0000\u0000\u0000\u0085\u0086\u0006\u0015\u0000"+
		"\u0000\u0086,\u0001\u0000\u0000\u0000\u0004\u0000y~\u0083\u0001\u0006"+
		"\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}