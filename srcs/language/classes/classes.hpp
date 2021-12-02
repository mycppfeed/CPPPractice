class EmptyClass { };

class SimpleClass_0 {
public:
    int x = 0;
};

class SimpleClass_1 {
private:
    int _x = 0;
public:
    int setX(int x) {
        auto tmp = _x;
        _x = x;
        return tmp;
    }

    int getX() const {
        return _x;
    }
};
